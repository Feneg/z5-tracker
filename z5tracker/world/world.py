'''
Item location management
'''

import importlib
import operator

from .. import rulesets

from .links import EVENTLOCATIONS

__all__ = 'DisplayGone', 'LocationTracker'


class DisplayGone(Exception):
    '''Raised when a called map display has been closed.'''
    pass


class LocationTracker(object):
    '''
    Item location tracker.

    Instance variables:
        rules: location ruleset
        itemlocations: item location list
        skulltulalocations: skulltula location list
        gui: list of registered map displays
        item_tracker: item tracker
    '''

    def __init__(self):
        self.recursion_block = False
        self.gui = []
        self.item_tracker = None
        self.reset()

    def reset(self) -> None:
        '''
        Recreate variables.
        '''

        self.rules = rulesets.Ruleset()
        self.itemlocations = self.rules.list_locations('item')
        self.skulltulalocations = self.rules.list_locations('skulltula')

    def register_gui(self, gui) -> None:
        '''
        Register GUI object.

        Args:
            gui: map display object
        '''

        self.gui.append(gui)

    def register_item_tracker(self, tracker) -> None:
        '''
        Register item tracker.

        This is used for location-dependent event items.

        Args:
           tracker: item tracker
        '''

        self.item_tracker = tracker

    def refresh_gui(self) -> None:
        '''
        Refresh registered map displays.
        '''

        guilist = self.gui
        self.gui = []
        for gui in guilist:
            try:
                gui.update_buttons()
            except DisplayGone:
                continue
            self.gui.append(gui)

    def check_availability(self, loctype: str, age: str = 'either') -> dict:
        '''
        Return list of locations and whether they are available.

        Args:
            loctype: 'item' or 'skulltula'
            age: 'child', 'adult' or 'either'
        Returns:
            dict: dictionary containing availability of locations
        '''

        assert loctype in ('item', 'skulltula')
        self.check_event_items()
        listing = (self.itemlocations if loctype == 'item'
                   else self.skulltulalocations)
        available = {}
        for location in listing:
            available[location] = self.rules.location_available(
                location, loctype, age)
        return available

    def dungeon_availability(self, dungeonname: str, loctype: str) -> str:
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

        self.check_event_items()
        return self.rules.dungeon_available(dungeonname, loctype)

    def check_visibility(self, loctype: str, age: str = 'either') -> dict:
        '''
        Return list of locations and whether they are visible.

        Args:
            loctype: 'item' or 'skulltulla'
            age: 'child', 'adult' or 'either'
        Returns:
            dict: dictionary containing visibility of locations
        '''

        assert loctype in ('item', 'skulltula')
        listing = (self.itemlocations if loctype == 'item'
                   else self.skulltulalocations)
        visible = {}
        for location in listing:
            visible[location] = self.rules.location_visible(
                location, loctype, age)
        return visible

    def add_item(self, itemname: str) -> None:
        '''
        Add item to current inventory.

        Args:
            itemname: identifier of item
        '''

        self.rules.add_item(itemname)
        self.refresh_gui()

    def remove_item(self, itemname: str) -> None:
        '''
        Remove item from current inventory.

        Args:
            itemname: identifier of item
        '''

        self.rules.remove_item(itemname)
        self.refresh_gui()

    def check_rule(self, rule: operator.methodcaller) -> bool:
        '''
        Check given rule.

        Args:
            rule: method to check with world state
        Return:
            bool: return value of check
        '''

        return self.rules.check_rule(rule)

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

        return self.rules.dungeon_locations(dungeonname)

    def dungeon_info(self, dungeonname: str) -> dict:
        '''
        Return info about given dungeon.

        Args:
            dungeonname: name of dungeon
        Returns:
            dict: {'keys': int, 'items': int, 'bosskey': bool}
        '''

        return self.rules.dungeon_info(dungeonname)

    def check_event_items(self) -> None:
        '''
        Check event items and update event items as needd.
        '''

        if self.recursion_block or self.item_tracker is None:
            return

        # Randomiser links
        events = self.rules.event_links()
        for eitem in events:
            self.recursion_block = True
            if events[eitem]:
                self.item_tracker[eitem].increase()
            else:
                for _ in range(self.item_tracker[eitem].inventory):
                    self.item_tracker[eitem].decrease()
            self.recursion_block = False

        # Manual links
        for event in EVENTLOCATIONS:

            # Make check.
            if event['type'] == 'location':
                check = True
                for subevent in event['name']:
                    check &= self.rules.location_available(
                        subevent, 'item', event['age'], just_region=True)
            else:
                assert False

            # Set event.
            item = self.item_tracker[event['event']]
            self.recursion_block = True
            if check:
                for _ in range(event['amount'] - item.inventory):
                    item.increase()
            else:
                for _ in range(item.inventory):
                    item.decrease()
            self.recursion_block = False
