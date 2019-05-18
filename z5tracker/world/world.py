'''
Item location management
'''

import importlib
import operator

from .. import rulesets

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
    '''

    def __init__(self):
        self.gui = []
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

    def check_availability(self, loctype: str) -> dict:
        '''
        Return list of locations and whether they are available.

        Args:
            loctype: 'item' or 'skulltula'
        Returns:
            dict: dictionary containing availability of locations
        '''

        assert loctype in ('item', 'skulltula')
        listing = (self.itemlocations if loctype == 'item'
                   else self.skulltulalocations)
        available = {}
        for location in listing:
            available[location] = self.rules.location_available(
                location, loctype)
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

        return self.rules.dungeon_available(dungeonname, loctype)

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

    def is_adult(self) -> bool:
        '''
        Check whether adult items are available.

        Returns:
            bool: True if adult items are available
        '''

        return self.rules.is_adult()

    def check_rule(self, rule: operator.methodcaller) -> bool:
        '''
        Check given rule.

        Args:
            rule: method to check with world state
        Return:
            bool: return value of check
        '''

        return self.rules.check_rule(rule)

    def check_access(self, location: str) -> bool:
        '''
        Check whether given location can be accessed.

        Args:
            location: either item location or game region
        Returns:
            bool: return value of check
        '''

        return self.rules.check_access(location)

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
