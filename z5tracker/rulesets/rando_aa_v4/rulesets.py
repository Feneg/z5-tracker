import operator
import os.path

from ...config import CONFIG
from ... import maps

from . import DungeonList as dungeons
from . import EntranceShuffle as entrances
from . import Item as items
from . import ItemList as itemlist
from . import HintList as hintlist
from . import LocationList as locationlist
from . import Region as regions
from . import Rules as rules
from . import Settings as settings
from . import State as state
from . import World as world

__all__ = 'Ruleset',


class Ruleset(object):
    '''
    Ruleset abstraction class.

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
        self.world = world.World(self.settings)
        self.world.load_regions_from_json(os.path.join(
            os.path.dirname(__file__), 'data', 'World', 'Overworld.json'))
        dungeons.create_dungeons(self.world)
        self.world.initialize_entrances()
        rules.set_rules(self.world)
        self.state = state.State(self.world)
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
        for equipment in itemlist.item_table:
            itm = itemlist.item_table[equipment]
            self.inventory[equipment] = items.Item(
                equipment, itm[1] == True, itm[1] == False,
                itm[0], itm[2], itm[3], self.world)

    def list_regions(self) -> set:
        '''
        Return list of all game regions.

        Returns:
            set: list of region names
        '''

        regions = {
            locationlist.location_table[l][3]
            for l in locationlist.location_table}
        return regions        

    def list_locations(self, loctype: str) -> list:
        '''
        Return list of all item locations.

        Args:
            loctype: 'item' or 'skulltula'
        Returns:
            list: list of location names
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
        if isinstance(listing[name], regions.Region):
            available = all(
                location.can_reach(self.state)
                for location in listing[name].locations)
        else:
            try:
                available = listing[name].can_reach(self.state)
            except AttributeError:
                available = False

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

        The item list includes the dungeon reward, but not Gossip Stones.

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
                if location.type in ('GossipStone', 'Event', 'Boss'):
                    continue
                if location.type == 'GS Token':
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
            len(locations)
            - ret['keys'] * (self.world.shuffle_smallkeys == 'dungeon')
            - ret['bosskey'] * (self.world.shuffle_bosskeys == 'dungeon')
            - len(dungeon.dungeon_items) * (
                self.world.shuffle_mapcompass == 'dungeon'))
        return ret

    def get_hint_items(self, pooltype: str) -> list:
        '''
        Return list of possible hint information.

        Args:
            pooltype: item, location or alwaysLocation
        Returns:
            list: list of hint strings
        '''

        if pooltype == 'all':
            return hintlist.hintTable
        return hintlist.getHintGroup(pooltype, self.world)
