'''
Dungeon management
'''

import configparser
import os.path
import json

from ..config import layout as storage
from ..items.lists import ITEMS
from .. import world

from .dungeonobj import DUNGEONS
from .dungeonobj import d as dobj
from .dungeonobj import image

__all__ = 'dobj', 'image', 'get_layout', 'DungeonTracker'


def get_layout() -> dict:
    '''
    Load (or create) dungeon layout.

    Returns:
        dict: dungeon layout in format {identifier: (column, row)}
    '''

    try:
        layout = storage.load('Dungeons')
    except (storage.NoConfig, configparser.Error):
        layout = {}
        layout['Dungeons'] = {}
        for dungeon in DUNGEONS:
            layout['Dungeons'][dungeon.identifier] = dungeon.location
        layout['Items'] = {}
        for item in ITEMS:
            layout['Items'][item.identifier] = item.location
        storage.new(layout)
        layout = storage.load('Dungeons')
    return layout


class DungeonTracker(dict):
    '''
    Dungeon tracker.
    '''

    def __init__(self, location_tracker: world.LocationTracker):
        '''
        Args:
            location_tracker: location tracker containing item placement rules
        '''

        layout = get_layout()

        super().__init__()
        for dungeon in DUNGEONS:
            dungeon.register_tracker(location_tracker)
            dungeon.location = layout[dungeon.identifier.lower()]
            self[dungeon.identifier] = dungeon
        data = storage.load_save()
        try:
            self.restore(data['Dungeons'])
        except KeyError:
            pass

    def reset(self) -> None:
        '''
        Reset all dungeon.
        '''

        for dungeon in self:
            self[dungeon].reset()

    def store(self) -> dict:
        '''
        Return current dungeon setup info for storage.

        Returns:
            inventory: dungeon setup info
        '''

        inventory = {}
        for dungeon in self:
            inventory[dungeon] = self[dungeon].store()
        return inventory

    def restore(self, inventory) -> None:
        '''
        Restore current dungeon setup from file.

        Args:
            inventory: information from file
        '''

        for dungeon in inventory:
            if dungeon in self:
                self[dungeon].restore(inventory[dungeon])
                try:
                    self[dungeon].gui.check_state(self[dungeon])
                except AttributeError:
                    pass
