'''
Item tracking object.
'''

import os.path
import typing

from ..config import CONFIG
from ..config.images import image
from .. import world

from .lists import INFO, REWARDS

__all__ = 'd', 'DUNGEONS'


class d(object):
    '''
    Dungeon item

    Instance variables:
        identifier: dungeon identifier string
        displayname: name displayed in UI
        icon: path to image file associated with dungeon
        keys: number of small keys in inventory
        bosskey: whether bosskey has been found
        items: number of items found
        reward: type of stone or medallion
        location: (column, row) location on display
        gui: associated display object
        max_keys: number of small keys in dungeon
        max_items: number of non-dungeon items in dungeon
        has_bosskey: True if dungeon has a boss key
    '''

    def __init__(
            self, dungeon: str, location: typing.Sequence[int]):
        '''
        Args:
            dungeon: internal dungeon name
            location: (column, row) coordinates on dungeon display
        '''

        self.identifier = dungeon
        self.displayname = INFO[dungeon]['name']
        self.icon = (
            image(INFO[dungeon]['icon'])[0] if INFO[dungeon]['icon'] else None)
        self.reset()
        self.location = location
        self.gui = None
        self.max_keys = None
        self.max_items = None
        self.has_bosskey = False

    def register_widget(self, widget: typing.Any) -> None:
        '''
        Store GUI object.

        Args:
            widget: object to store
        Writes:
            gui
        '''

        self.gui = widget

    def register_tracker(self, location_tracker: world.LocationTracker) -> None:
        '''
        Register location tracker containing placement rules.

        Args:
            location_tracker: tracker to register
        '''

        self.location_tracker = location_tracker
        dungeon_info = self.location_tracker.dungeon_info(self.identifier)
        self.max_keys = dungeon_info['keys']
        self.max_items = dungeon_info['items']
        self.has_bosskey = dungeon_info['bosskey']
        for _ in range(self.keys):
            self.location_tracker.add_item(
                'Small Key ({0:s})'.format(self.identifier))
        if self.bosskey:
            self.location_tracker.add_item(
                'Boss Key ({0:s})'.format(self.identifier))

    def reset(self) -> None:
        '''
        Reset dungeon.
        '''

        self.keys = 0
        self.bosskey = False
        self.items = 0
        self.reward = '?'
        try:
            self.gui.check_state(self)
        except AttributeError:
            pass

    def key_up(self, *args) -> None:
        '''
        Increase key counter.
        '''

        if self.keys < self.max_keys:
            self.keys += 1
            self.location_tracker.add_item(
                'Small Key ({0:s})'.format(self.identifier))
        self.gui.check_state(self)

    def key_down(self, *args) -> None:
        '''
        Decrease key counter.
        '''

        if self.keys > 0:
            self.keys -= 1
            self.location_tracker.remove_item(
                'Small Key ({0:s})'.format(self.identifier))
        self.gui.check_state(self)

    def toggle_bosskey(self, *args) -> None:
        '''
        Toggle bosskey.
        '''

        self.bosskey = not self.bosskey
        tracker_cmd = (self.location_tracker.add_item if self.bosskey
                       else self.location_tracker.remove_item)
        tracker_cmd('Boss Key ({0:s})'.format(self.identifier))
        self.gui.check_state(self)

    def item_up(self, *args) -> None:
        '''
        Increase item counter.
        '''

        if self.items < self.max_items:
            self.items += 1
        self.gui.check_state(self)

    def item_down(self, *args) -> None:
        '''
        Decrease item counter.
        '''

        if self.items > 0:
            self.items -= 1
        self.gui.check_state(self)

    def remaining(self) -> int:
        '''
        Return remaining items.

        Returns:
           int: still to be found number of items
        '''

        return self.max_items - self.items

    def cycle_reward(self, forward: bool) -> None:
        '''
        Cycle through rewards.

        Args:
            forward: True cycles forward, False backwards
        '''

        rewardlist = tuple(REWARDS)
        idx = rewardlist.index(self.reward)
        if forward:
            idx += 1
            idx %= len(REWARDS)
        else:
            idx -= 1
            if idx < 0:
                idx = len(REWARDS) - 1
        self.reward = rewardlist[idx]
        self.gui.check_state(self)

    def store(self) -> dict:
        '''
        Return contained info for saving.

        Returns:
            dict: dictionary with dungeon info
        '''

        data = {
            'identifier': self.identifier,
            'keys': self.keys,
            'bosskey': self.bosskey,
            'items': self.items,
            'reward': self.reward,
        }
        return data

    def restore(self, data: dict) -> None:
        '''
        Restore contained info.

        Args:
            data: dictionary with required info
        '''

        mapping = 'identifier', 'keys', 'bosskey', 'items', 'reward'
        for datum in mapping:
            try:
                self.__setattr__(datum, data[datum])
            except AttributeError:
                pass
            if datum in ('keys', 'bosskey'):
                keytype = 'Small Key' if datum == 'keys' else 'Boss Key'
                keyattr = self.keys if datum == 'keys' else self.bosskey
                for _ in range(int(keyattr)):
                    self.location_tracker.add_item(
                        '{0:s} ({1:s})'.format(keytype, self.identifier))


DUNGEONS = (
    d('Deku Tree', (0, 0)), d('Dodongos Cavern', (0, 1)),
    d('Jabu Jabus Belly', (0, 2)), d('Ice Cavern', (0, 3)),
    d('Bottom of the Well', (0, 4)), d('Gerudo Training Grounds', (0, 5)),
    d('Forest Temple', (1, 0)), d('Fire Temple', (1, 1)),
    d('Water Temple', (1, 2)), d('Shadow Temple', (1, 3)),
    d('Spirit Temple', (1, 4)), d('Ganons Castle', (1, 5))
)
