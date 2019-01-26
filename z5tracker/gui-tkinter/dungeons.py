'''
Dungeon display.
'''

import tkinter as tk
import tkinter.ttk as ttk
import typing

from ..config import CONFIG
from ..config import layout as storage
from .. import dungeons
from ..dungeons.lists import INFO, IMG, REWARDS
from ..items.itemobj import image

from . import misc

__all__ = 'DungeonWindow',


class DungeonWindow(tk.Toplevel):
    '''
    Dungeon check display.

    Instance variables:
        tracker: dungeon tracker object
        layout: dungeon layout in display
        helpertext: helper text variable
        scaling: up- and downscale factors for objects
    '''

    def __init__(self, tracker: dungeons.DungeonTracker):
        '''
        Args:
            tracker: dungeon tracker object
        '''

        super().__init__()
        self.title('Dungeons')

        self.tracker = tracker

        self.frame = ttk.Frame(self)
        self.frame.grid(column=0, row=0, sticky=misc.A)
        self.helpertext = tk.StringVar()
        self.helper = ttk.Label(
            self, textvariable=self.helpertext,
            font=('Arial', int(12 * CONFIG['icon_size'])))
        self.helper.grid(column=0, row=1, sticky=tk.S)

        self.scaling = _scale_factors()

        buttonstyle = ttk.Style()
        buttonstyle.configure('Dungeonbutton.TButton', relief=tk.FLAT)

        for dungeon in self.tracker:
            self._dungeon_display(self.tracker[dungeon])

    def _dungeon_display(self, dungeon: dungeons.dobj) -> None:
        '''
        Make and place single dungeons display object.

        Args:
            dungeon: dungeon object
        Writes:
            buttons
        '''

        widget = Dungeon(dungeon, self.frame, self.scaling)
        widget.bind(
            '<Enter>', lambda _: self.helpertext.set(dungeon.displayname))
        widget.bind(
            '<Leave>', lambda _: self.helpertext.set(''))

        for button in widget.buttons:
            button.bind(
                '<ButtonRelease-1>',
                lambda _: storage.autosave('Dungeons', self.tracker),
                add='+')
            button.bind(
                '<ButtonRelease-3>',
                lambda _: storage.autosave('Dungeons', self.tracker),
                add='+')

        widget.grid(column=dungeon.location[0], row=dungeon.location[1],
                    sticky=tk.N+tk.W)
        dungeon.register_widget(widget)

    def reset(self) -> None:
        '''
        Reset dungeons to default.
        '''

        self.tracker.reset()


class Dungeon(ttk.Frame):
    '''
    Single dungeon display object.
    '''

    def __init__(
            self, dungeon: dungeons.dobj, parent: ttk.Frame,
            scaling: (int, int)):
        '''
        dungeon: dungeon object
        parent: parent widget for object
        scaling: button scale
        '''

        self.scaling = scaling
        scale = scaling[0] / scaling[1]

        super().__init__(parent)
        self.child = ttk.Label(self)
        self.child.grid(column=0, row=0, sticky=misc.A)

        icon = (
            tk.PhotoImage(file=dungeon.icon, master=parent)
            if dungeon.icon else None)
        icon = self._icon_scale(icon)
        self.pic = ttk.Label(self.child, image=icon)
        self.pic.grid(column=0, row=0)
        self.icon = icon

        self.rewardname = '?'
        self.rewardimg = REWARDS['?']
        self.rewardicon = tk.PhotoImage(
            file=image(REWARDS['?'])[0], master=self)
        self.rewardicon = self._icon_scale(self.rewardicon)
        self.reward = tk.Canvas(
            self.child, height=32 * scale, width=32 * scale)
        self.rewardid = self.reward.create_image(
            0, 0, anchor=tk.NW, image=self.rewardicon)
        self.reward.bind(
            '<ButtonRelease-1>', lambda _: dungeon.cycle_reward(True))
        self.reward.bind(
            '<ButtonRelease-3>', lambda _: dungeon.cycle_reward(False))
        if INFO[dungeon.identifier]['reward']:
            self.reward.grid(column=2, row=0)

        self.bosskeyicon = tk.PhotoImage(
            file=image(IMG['bosskey'])[0], master=parent)
        self.bosskeyicon = self._icon_scale(self.bosskeyicon)
        self.bosskey = tk.Canvas(
            self.child, height=32 * scale, width=32 * scale)
        self.bosskeyid = self.bosskey.create_image(
            0, 0, anchor=tk.NW, image=self.bosskeyicon)
        self.bosskey.bind('<ButtonRelease-1>', dungeon.toggle_bosskey)
        self.bosskey.bind('<ButtonRelease-3>', dungeon.toggle_bosskey)
        self.hasbosskey = False
        if dungeon.has_bosskey:
            self.hasbosskey = True
            self.bosskey.grid(column=3, row=0)

        self.keyicon = tk.PhotoImage(file=image(IMG['key'])[0], master=parent)
        self.keyicon = self._icon_scale(self.keyicon)
        self.key = tk.Canvas(
            self.child, height=32 * scale, width=48 * scale)
        self.keyimg = self.key.create_image(
            0, 0, anchor=tk.NW, image=self.keyicon)
        self.keytext = self.key.create_text(
            48 * scale, 32 * scale, anchor=tk.SE, text='')
        self.key.bind('<ButtonRelease-1>', dungeon.key_up)
        self.key.bind('<ButtonRelease-3>', dungeon.key_down)
        self.haskeys = False
        if dungeon.max_keys > 0:
            self.haskeys = True
            self.key.grid(column=2, columnspan=2, row=1)

        self.itemicon = tk.PhotoImage(
            file=image(IMG['chest_full'])[0], master=parent)
        self.itemicon = self._icon_scale(self.itemicon)
        self.item = tk.Canvas(
            self.child, height=32 * scale, width=48 * scale)
        self.itemimg = self.item.create_image(
            0, 0, anchor=tk.NW, image=self.itemicon)
        self.itemtext = self.item.create_text(
            48 * scale, 32 * scale, anchor=tk.SE, text='')
        self.item.bind('<ButtonRelease-1>', dungeon.item_up)
        self.item.bind('<ButtonRelease-3>', dungeon.item_down)
        self.item.grid(column=0, columnspan=2, row=1)

        self.buttons = self.reward, self.bosskey, self.key, self.item

        self.check_state(dungeon)

    def check_state(self, dungeon: dungeons.dobj) -> None:
        '''
        Check button state and make adjustments if necessary.

        Args:
            dungeon: dungeon object
        '''

        # Check whether the bosskey button should be disabled.
        if self.hasbosskey:
            self.bosskey.delete(self.bosskeyid)
            self.bosskeyicon = tk.PhotoImage(
                file=image(IMG['bosskey'])[0], master=self)
            self.bosskeyicon = self._icon_scale(self.bosskeyicon)
            if not dungeon.bosskey:
                for x in range(self.bosskeyicon.width()):
                    for y in range(self.bosskeyicon.height()):
                        bw = sum(self.bosskeyicon.get(x, y)) // 3
                        if bw in (0, 255):
                            continue
                        self.bosskeyicon.put(
                            '#{0:02x}{0:02x}{0:02x}'.format(bw), (x, y))
            self.bosskey.create_image(
                0, 0, anchor=tk.NW, image=self.bosskeyicon)

        # Check whether reward image needs to be changed.
        if self.rewardname != dungeon.reward:
            self.rewardname = dungeon.reward
            self.rewardimg = REWARDS[dungeon.reward]
            self.rewardicon = tk.PhotoImage(
                file=image(self.rewardimg)[0], master=self)
            self.rewardicon = self._icon_scale(self.rewardicon)
            self.reward.delete(self.rewardid)
            self.reward.create_image(0, 0, anchor=tk.NW, image=self.rewardicon)

        # Check numbers.
        scale = self.scaling[0] / self.scaling[1]
        self.key.delete(self.keytext)
        self.keytext = self.key.create_text(
            48 * scale, 32 * scale, anchor=tk.SE,
            font=('Arial Black', int(16 * scale)), text=str(dungeon.keys))
        self.item.delete(self.itemtext)
        itemfont = (('Arial Black', int(8 * scale)) if dungeon.remaining() > 9
                    else ('Arial Black', int(16 * scale)))
        self.itemtext = self.item.create_text(
            48 * scale, 32 * scale, anchor=tk.SE, font=itemfont,
            text=str(dungeon.remaining()))
        newchest = 'chest_full' if dungeon.remaining() > 0 else 'chest_empty'
        self.itemicon = tk.PhotoImage(file=image(IMG[newchest])[0], master=self)
        self.itemicon = self._icon_scale(self.itemicon)
        self.item.delete(self.itemimg)
        self.itemimg = self.item.create_image(
            0, 0, anchor=tk.NW, image=self.itemicon)

    def _icon_scale(self, icon: tk.PhotoImage) -> tk.PhotoImage:
        '''
        Rescale icon.

        Args:
            icon: icon to be rescaled
        Returns:
            tk.PhotoImage: rescaled icon
        '''

        if self.scaling[0] != 1:
            icon = icon.zoom(self.scaling[0], self.scaling[0])
        if self.scaling[1] != 1:
            icon = icon.subsample(self.scaling[1], self.scaling[1])
        return icon


def _scale_factors() -> (int, int):
    '''
    Calculate up- and downscale factor.

    Returns:
        int: upscale factor
        int: downscale factor
    '''

    scaling = CONFIG['icon_size']
    for up in range(1, 1000):
        if not (scaling * up) % 1:
            upscale = int(scaling * up)
            break
    else:
        CONFIG.set('icon_size', 1)
        assert False
    downscale = int(upscale // scaling)
    return upscale, downscale
