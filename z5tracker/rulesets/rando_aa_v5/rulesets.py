import operator
import os.path
import typing

from ...config import CONFIG
from ... import maps

from . import DungeonList as dungeons
from . import Item as items
from . import ItemList as itemlist
from . import ItemPool as itempool
from . import HintList as hintlist
from . import Location as locationclass
from . import LocationList as locationlist
from . import Region as regions
from . import Rules as rules
from . import Settings as settings
from .SettingsList import logic_tricks
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

        # Load game settings from rules string.
        self.settings = settings.Settings({})
        self.settings.update_with_settings_string(CONFIG['rule_string'])

        # Special consideration for difficult moves. Something like is is also
        # done by the randomiser.
        for trick in logic_tricks:
            self.settings.__dict__[logic_tricks[trick]['name']] = (
                logic_tricks[trick]['name']
                in self.settings.__dict__['allowed_tricks'])

        # Set up game data.
        self.world = world.World(self.settings)
        self.world.id = 0
        glitch_rules = ('Glitched World' if self.world.logic_rules == 'glitched'
                        else 'World')
        self.world.load_regions_from_json(os.path.join(
            os.path.dirname(__file__), 'data', glitch_rules, 'Overworld.json'))

        # Set up dungeons.
        dungeons.create_dungeons(self.world)

        # Connect entrances to create a coherent world. If entrance
        # randomisation is ever supported, this will need to be skipped. The
        # randomiser used to call this but now instead gets here via
        # set_entrances() (which we most certainly don't want to call.)
        self.world.initialize_entrances()

        # Set item location rules.
        rules.set_rules(self.world)

        # Create game state.
        self.state = state.State(self.world)

        # Permanently disable certain location. This is a little bit hacky,
        # but seems to be one of two possible solution. The other one is only
        # just slightly less hacky.
        if not CONFIG['show_disabled']:
            for loc in self.world.get_locations():
                if loc.disabled == locationclass.DisableType.PENDING:
                    loc.locked = True

        # Load our own internal data.
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

        # Create our own game state information.
        self.inventory = {}
        for equipment in itemlist.item_table:
            itm = itemlist.item_table[equipment]
            self.inventory[equipment] = items.Item(equipment, self.world)

    def list_regions(self) -> set:
        '''
        Return list of all game regions.

        Returns:
            set: list of region names
        '''

        regions = {
            locationlist.location_table[l][4][0]
            for l in locationlist.location_table
            if locationlist.location_table[l][4]}
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

    def location_available(
            self, name: str, loctype: str, age: str = 'either',
            state: state.State = None, just_region: bool = False) -> bool:
        '''
        Check whether given item location is available.

        Args:
            name: name of item location
            loctype: 'item' or 'skulltula'
            age: 'child', 'adult' or 'either'
            state: if given, use this state instead of default one
            just_region: if 'name' is a region, just check region availability
        Returns:
            bool: True if location is available
        '''

        assert loctype in ('item', 'skulltula')
        listing = self.items if loctype == 'item' else self.skulls
        usestate = self.state if state is None else state
        if isinstance(listing[name], regions.Region) and not just_region:
            available = all(
                usestate.can_reach(location, age=age)
                for location in listing[name].locations)
        else:
            try:
                available = usestate.can_reach(listing[name], age=age)
            except AttributeError:
                available = False

        return available

    def dungeon_available(self, name: str, loctype: str) -> str:
        '''
        Check to which degree dungeon is clearable.

        This assumes that all keys are available. It hence only checks for
        required items.

        Args:
            dungeonname: name of dungeon
            itemtype: 'item' or 'skulltula'
        Returns:
            bool: True of all locations are available with all keys
        '''

        skeyname = 'Small Key ({0:s})'.format(name)
        bkeyname = 'Boss Key ({0:s})'.format(name)
        info = self.dungeon_info(name)
        fullstate = self.state.copy()
        if fullstate.world.shuffle_smallkeys in ('dungeon', 'vanilla'):
            fullstate.prog_items[skeyname] = info['keys']
        if (
                info['bosskey'] and
                fullstate.world.shuffle_bosskeys in ('dungeon', 'vanilla')):
            fullstate.prog_items[bkeyname] = 1
        fullstate.clear_cache()
        restrict = operator.methodcaller('startswith', name)
        events = self.event_links(fullstate, restrict)
        changed = True
        while changed:
            changed = False
            for eitem in events:
                if events[eitem] and not fullstate.prog_items[eitem]:
                    fullstate.prog_items[eitem] = 1
                    changed = True
            fullstate.clear_cache()
            events = self.event_links(fullstate, restrict)
        locs = self.dungeon_locations(name)
        locs = locs[0] if loctype == 'item' else locs[1]
        listing = self.items if loctype == 'item' else self.skulls
        try:
            available = all(
                fullstate.can_reach(listing[l], age='either') for l in locs)
        except KeyError:
            available = False
        return available

    def location_visible(
            self, name: str, loctype: str, age: str = 'either') -> bool:
        '''
        Check whether given item location is visible.

        Args:
            name: name of item location
            loctype: 'item' or 'skulltula'
            age: 'child', 'adult' or 'either'
        Returns:
            bool: True if location is visible
        '''

        assert loctype in ('item', 'skulltula')
        listing = self.items if loctype == 'item' else self.skulls
        if isinstance(listing[name], regions.Region):
            visible = any(
                location.has_preview() for location in listing[name].locations)
            visible &= self.state.can_reach(listing[name], age=age)
        else:
            try:
                visible = listing[name].has_preview()
            except AttributeError:
                visible = False
            visible &= self.state.can_reach(
                listing[name].parent_region, age=age)

        return visible

    def add_item(self, itemname: str) -> None:
        '''
        Add item to current inventory.

        Args:
            itemname: identifier of item
        '''

        self.state.collect(self.inventory[itemname])
        self.state.clear_cache()

    def remove_item(self, itemname: str) -> None:
        '''
        Remove item from current inventory.

        Args:
            itemname: identifier of item
        '''

        self.state.remove(self.inventory[itemname])
        self.state.clear_cache()

    def check_rule(self, rule: operator.methodcaller) -> bool:
        '''
        Check given rule.

        Args:
            rule: method to check with world state
        Return:
            bool: return value of check
        '''

        return rule(self.state)

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
            - ret['keys'] * (
                self.world.shuffle_smallkeys in ('dungeon', 'vanilla'))
            - ret['bosskey'] * (
                self.world.shuffle_bosskeys in ('dungeon', 'vanilla'))
            - len(dungeon.dungeon_items) * (
                self.world.shuffle_mapcompass in ('dungeon', 'vanilla')))
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

    def get_hint_distribution(self) -> str:
        '''
        Return hint distribution type.

        Returns:
            str: 'useless', 'balanced', 'strong', 'very_strong', 'tournament'
        '''

        return self.world.hint_dist

    def event_links(self, state: state.State = None, restrict = None) -> dict:
        '''
        Return availability of event items.

        Args:
            state: if not None, use this state instead of default
            restrict: only return events passing this test
        Returns:
            dict: {'event item': bool}
        '''

        eventlocations = {}
        eventlinks = itempool.eventlocations
        if restrict is not None:
            events = {
                eventlinks[eloc] for eloc in eventlinks if restrict(eloc)}
        else:
            events = set(eventlinks.values())
        for eitem in events:
            eventlocations[eitem] = any(
                self.location_available(eloc, 'item', state=state)
                for eloc in eventlinks if eventlinks[eloc] == eitem)
        return eventlocations
