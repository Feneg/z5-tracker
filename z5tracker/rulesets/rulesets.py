import importlib
import operator

from ..config import CONFIG
from .. import maps

try:
    baseclasses = importlib.import_module('.BaseClasses', package=__package__)
except ModuleNotFoundError:
    baseclasses = importlib.import_module(
        '.{0:s}.BaseClasses'.format(CONFIG['ruleset']), package=__package__)

try:
    dungeons = importlib.import_module('.Dungeons', package=__package__)
except ModuleNotFoundError:
    dungeons = importlib.import_module(
        '.{0:s}.Dungeons'.format(CONFIG['ruleset']), package=__package__)

try:
    entrances = importlib.import_module('.EntranceShuffle', package=__package__)
except ModuleNotFoundError:
    entrances = importlib.import_module(
        '.{0:s}.EntranceShuffle'.format(CONFIG['ruleset']), package=__package__)

try:
    items = importlib.import_module('.Items', package=__package__)
except ModuleNotFoundError:
    items = importlib.import_module(
        '.{0:s}.Items'.format(CONFIG['ruleset']), package=__package__)

try:
    regions = importlib.import_module('.Regions', package=__package__)
except ModuleNotFoundError:
    regions = importlib.import_module(
        '.{0:s}.Regions'.format(CONFIG['ruleset']), package=__package__)

try:
    rules = importlib.import_module('.Rules', package=__package__)
except ModuleNotFoundError:
    rules = importlib.import_module(
        '.{0:s}.Rules'.format(CONFIG['ruleset']), package=__package__)

try:
    settings = importlib.import_module('.Settings', package=__package__)
except ModuleNotFoundError:
    settings = importlib.import_module(
        '.{0:s}.Settings'.format(CONFIG['ruleset']), package=__package__)

__all__ = 'Ruleset',


class Ruleset(object):
    '''
    Ruleset abstraction class.

    I don't really know why I abstract in the first place, but it makes me more
    comfortable.

    Instance variables:
        items: item locations
        skulls: skulltula locations
        inventory: item inventory
    '''

    def __init__(self):
        defaults = {}
        for info in settings.setting_infos:
            if 'default' in info.args_params:
                defaults[info.name] = info.args_params['default']
            else:
                defaults[info.name] = None
        self.settings = settings.Settings(defaults)
        self.settings.update_with_settings_string(CONFIG['rule_string'])
        self.world = baseclasses.World(self.settings)
        regions.create_regions(self.world)
        dungeons.create_dungeons(self.world)
        entrances.link_entrances(self.world)
        rules.global_rules(self.world)
        self.state = baseclasses.CollectionState(self.world)
        self.items = {}
        self.skulls = {}
        for i in self.world.regions:
            for j in i.locations:
                if j.name in maps.SKULLTULALOCATIONS:
                    self.skulls[j.name] = j
                elif j.name in maps.ITEMLOCATIONS:
                    self.items[j.name] = j
            else:
                if i.name in maps.SKULLTULALOCATIONS:
                    self.skulls[i.name] = i
                elif i.name in maps.ITEMLOCATIONS:
                    self.items[i.name] = i

        self.inventory = {}
        for equipment in items.item_table:
            self.inventory[equipment] = baseclasses.Item(
                equipment, *items.item_table[equipment])

    def list_locations(self, loctype: str) -> list:
        '''
        Return list of all item locations.

        loctype: 'item' or 'skulltula'
        '''

        assert loctype in ('item', 'skulltula')
        listing = self.items if loctype == 'item' else self.skulls
        return list(listing.keys())

    def location_available(self, name: str, loctype: str) -> bool:
        '''
        Check whether given item location is available.

        Args:
            name: name of item location
            loctype: 'item' or 'skulltula'
        Returns:
            bool: True if location is available
        '''

        assert loctype in ('item', 'skulltula')
        listing = self.items if loctype == 'item' else self.skulls
        if isinstance(listing[name], baseclasses.Region):
            available = all(
                location.can_reach(self.state)
                for location in listing[name].locations)
        else:
            available = listing[name].can_reach(self.state)

        return available

    def add_item(self, itemname: str) -> None:
        '''
        Add item to current inventory.

        Args:
            itemname: identifier of item
        '''

        self.state.collect(self.inventory[itemname])

    def remove_item(self, itemname: str) -> None:
        '''
        Remove item from current inventory.

        Args:
            itemname: identifier of item
        '''

        self.state.remove(self.inventory[itemname])

    def is_adult(self) -> bool:
        '''
        Check whether adult items are available.

        Returns:
            bool: True if adult items are available
        '''

        return self.state.is_adult()

    def check_rule(self, rule: operator.methodcaller) -> bool:
        '''
        Check given rule.

        Args:
            rule: method to check with world state
        Return:
            bool: return value of check
        '''

        return rule(self.state)

    def check_access(self, location: str) -> bool:
        '''
        Check whether given location can be accessed.

        Args:
            location: either item location, game region or region connector
        Returns:
            bool: return value of check
        '''

        for loctype in ('get_region', 'get_entrance', 'get_location'):
            loccall = operator.methodcaller(loctype, location)
            try:
                locobject = loccall(self.world)
            except RuntimeError:
                continue
            break
        else:
            raise

        return locobject.can_reach(self.state)

    def dungeon_locations(self, dungeonname: str) -> (list, list):
        '''
        Return list of locations in given dungeon.

        The item list includes the dungeon reward.

        Args:
            dungeonname: name of dungeon
        Returns:
            list: list of item locations
            list: list of skulltula locations
        '''

        for dungeon in self.world.dungeons:
            if dungeon.name == dungeonname:
                break
        else:
            assert False

        items = []
        spiders = []
        for region in dungeon.regions:
            for location in region.locations:
                if location.name.startswith('GS '):
                    spiders.append(location.name)
                    continue
                maploc = maps.ITEMLOCATIONS[location.name]
                if not maploc['maps']:
                    continue
                if 'restriction' in maploc:
                    if maploc['restriction'] == 'scrubshuffle':
                        if self.world.shuffle_scrubs == 'off':
                            continue
                items.append(location.name)
        return items, spiders

    def dungeon_info(self, dungeonname: str) -> dict:
        '''
        Return info about given dungeon.

        Args:
            dungeonname: name of dungeon
        Returns:
            dict: {'keys': int, 'items': int, 'bosskey': bool}
        '''

        for dungeon in self.world.dungeons:
            if dungeon.name == dungeonname:
                break
        else:
            assert False

        ret = {}
        ret['keys'] = len(dungeon.small_keys)
        ret['bosskey'] = bool(dungeon.boss_key)
        locations, _ = self.dungeon_locations(dungeonname)
        ret['items'] = (
            len(locations) - 1
            - ret['keys'] - ret['bosskey'] - len(dungeon.dungeon_items))
        return ret
