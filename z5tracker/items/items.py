'''
Item management
'''

import configparser
import os.path
import json

from ..config.images import image
from ..config import layout as storage
from ..dungeons.dungeonobj import DUNGEONS
from .. import world

from .itemobj import i as iobj
from .lists import ITEMS

__all__ = 'iobj', 'image', 'get_layout', 'ItemTracker'


def get_layout() -> dict:
    '''
    Load (or create) item layout.

    Returns:
        dict: item layout in format {identifier: (column, row)}
    '''

    try:
        layout = storage.load('Items')
    except (storage.NoConfig, configparser.Error):
        layout = {'Items': {}, 'Dungeons': {}}
        for item in ITEMS:
            layout['Items'][item.identifier] = item.location
        for dungeon in DUNGEONS:
            layout['Dungeons'][dungeon.identifier] = dungeon.location
        storage.new(layout)
        layout = storage.load('Items')
    return layout


class ItemTracker(dict):
    '''
    Inventory item tracker.
    '''

    def __init__(self, location_tracker: world.LocationTracker):
        '''
        Args:
            location_tracker: location tracker containing item placement rules
        '''

        layout = get_layout()

        super().__init__()
        delayed_link = []
        for item in ITEMS:
            item.register_tracker(location_tracker)
            try:
                item.location = layout[item.identifier.lower()]
            except KeyError:
                pass
            for linkobj in item.link:
                try:
                    item.register_link(self[linkobj[0]])
                except KeyError:
                    delayed_link.append((item.identifier, linkobj))
            self[item.identifier] = item
        for to_link in delayed_link:
            self[to_link[0]].register_link(self[to_link[1][0]])
        data = storage.load_save()
        try:
            self.restore(data['Items'])
        except KeyError:
            pass

    def reset(self) -> None:
        '''
        Reset all items.
        '''

        for item in self:
            self[item].reset()

    def store(self) -> dict:
        '''
        Return current item setup info for storage.

        Returns:
            inventory: item setup info
        '''

        inventory = {}
        for item in self:
            inventory[item] = self[item].inventory
        return inventory

    def restore(self, inventory) -> None:
        '''
        Restore current item setup from file.

        Args:
            inventory: information from file
        '''

        for item in inventory:
            if item in self:
                self[item].restore_inventory(inventory[item])
                try:
                    self[item].gui.check_state(self[item])
                except AttributeError:
                    pass
