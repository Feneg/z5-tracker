'''
Item tracking object.
'''

import operator
import os.path
import typing

from ..config.images import image
from .. import world

__all__ = 'i',


class i(object):
    '''
    Inventory item

    Progressive items are listed as one.

    Instance variables:
        length: number of item progressions
        identifier: item identifier string
        displayname: name(s) displayed in UI
        icon: path to image file(s) associated with item
        link: items (and tresholds) linked with this item
        linked_items: actual item objects linked with this items
        inventory: number of items in inventory
        location: (column, row) location on display
        gui: associated display object
        location_tracker: location tracker containing item placement rules
    '''

    def __init__(
            self, item: str, location: typing.Sequence[int],
            display: typing.Sequence[str], icon: typing.Sequence[str],
            link: tuple = (), override: typing.Callable[[str], None] = None,
            default: int = 0):
        '''
        Args:
            item: internal item name
            location: (column, row) coordinates on item display
            display: displayed item name(s)
            icon: item icon(s)
            link: link other items' progression to this one
            override: function called to implement special behaviour
            default: default inventory setting
        '''

        assert len(display) == len(icon)
        self.length = len(display)
        self.identifier = item
        self.displayname = display
        self.icon = tuple(image(i) for i in icon if i != '<stub>')
        self.link = link
        self.linked_items = {}
        self.override = override
        self.default = default
        self.location_tracker = None
        self.inventory = default
        self.location = location
        self.gui = None

    def register_tracker(self, tracker: world.LocationTracker) -> None:
        '''
        Store item location tracker.

        Args:
            tracker: location tracker containing item placement rules
        Writes:
            location_tracker
        '''

        self.location_tracker = tracker

    def register_button(self, button: typing.Any) -> None:
        '''
        Store GUI object.

        Args:
            button: object to store
        Writes:
            gui
        '''

        self.gui = button

    def index(self) -> int:
        '''
        Return current image index.

        Returns:
            int: index used for sequence attributes
        '''

        idx = self.inventory if self.inventory < 1 else self.inventory - 1
        return idx

    def display(self) -> str:
        '''
        Return currently applicable item display string.

        Returns:
            str: name to be displayed in application
        '''

        self.gui.check_state(self)
        idx = self.index()
        item_name = self.displayname[idx]
        if self.icon[idx][1] is not None and self.state():
            item_name = '{0:s} ({1:s})'.format(
                item_name, str(self.icon[idx][1]))
        return item_name

    def state(self) -> bool:
        '''
        Return current state of item.

        Returns:
            str: True if item is active, else False
        '''

        return self.inventory > 0

    def increase(self, *args) -> None:
        '''
        Left-click on item
        '''

        if self.inventory < self.length:
            self.inventory += 1
            self.location_tracker.add_item(self.identifier)
        self._set_links()
        if self.icon:
            self.gui.check_state(self)

    def decrease(self, *args) -> None:
        '''
        Right-click on item
        '''
        
        if self.inventory > 0:
            self.inventory -= 1
            self.location_tracker.remove_item(self.identifier)
        self._set_links()
        if self.icon:
            self.gui.check_state(self)

    def reset(self) -> None:
        '''
        Reset item.
        '''

        to_remove = self.inventory - self.default
        if to_remove > 0:
            for _ in range(to_remove):
                self.decrease(_)
        elif to_remove < 0:
            for _ in range(-to_remove):
                self.increase(_)
        self.gui.check_state(self)

    def restore_inventory(self, quantity: int) -> None:
        '''
        Set inventory number.

        Args:
            quantity: number to set inventory to
        '''

        self.inventory = quantity
        for _ in range(quantity):
            self.location_tracker.add_item(self.identifier)

    def register_link(self, linkobject) -> None:
        '''
        Add linked object.

        Args:
            linkobject: item object to link with
        '''

        linkobject.register_tracker(self.location_tracker)
        self.linked_items[linkobject.identifier] = linkobject

    def _set_links(self) -> None:
        '''
        Set state of linked items.
        '''

        for link in self.link:
            if self.inventory >= link[1]:
                self.linked_items[link[0]].increase()
            else:
                self.linked_items[link[0]].decrease()
