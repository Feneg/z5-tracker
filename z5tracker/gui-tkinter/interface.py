'''
Program GUI
'''

import re
import threading
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as tkmbox
import tkinter.ttk as ttk
import typing

from ..config import layout as storage
from ..config import windows as window_layout
from .. import dungeons as dungeon_tracker
from .. import items as item_tracker
from .. import world as location_tracker

from . import config
from . import dungeons as dungeon_gui
from . import hints
from . import items as item_gui
from . import maps
from . import menu

__all__ = 'GraphicalInterface',


class GraphicalInterface(object):
    '''
    Main access point for everything GUI related.

    Instance variables:
        gui_root: tkinter framework root object
        gui_style: tkinter style class
        gui_app: tkinter application object
        commands: methods used to create new windows
        windows: collection of child windows
        item_tracker: inventory item tracker
        location tracker: item location tracker
        restart: indicator for required restart
    '''

    def __init__(self):
        '''
        Initialise GUI.
        '''

        self.gui_root = tk.Tk()
        self.gui_root.call('tk', 'scaling', 1)
        self.gui_style = ttk.Style()
        # self.gui_style.theme_use('clam')
        self.gui_app = ttk.Frame(self.gui_root)
        self.gui_root.withdraw()
        self.restart = threading.Event()

        self.location_tracker = location_tracker.LocationTracker()
        self.item_tracker = item_tracker.ItemTracker(self.location_tracker)

        self.commands = {
            'items': self._open_items,
            'itemreset': self._reset_items,
            'itemmap': self._open_itemmap,
            'itemmap_c': self._open_itemmap,
            'itemmap_a': self._open_itemmap,
            'skullmap': self._open_skullmap,
            'skullmap_c': self._open_skullmap,
            'skullmap_a': self._open_skullmap,
            'dungeons': self._open_dungeons,
            'hints': self._open_hints,
            'config': self._open_config,
            'load': self._load,
            'save': self._save,
            'quit': self.quit,
            }

        self.windows = {
            'menu': menu.MenuWindow(commands=self.commands),
            'items': None,
            'itemmap_c': None,
            'itemmap_a': None,
            'skullmap_c': None,
            'skullmap_a': None,
            'dungeons': None,
            'config': None,
            'hints': None,
            }

        self._restore_windows()
        self._prepare_windows()
        self.windows['menu'].protocol('WM_DELETE_WINDOW', self.quit)

    def _restore_windows(self) -> None:
        '''
        Restore previously stored window layout.
        '''

        layout = window_layout.load()
        for window in layout:
            if self.windows[window] is None:
                self.commands[window]()
            self.windows[window].geometry(
                '+{0:d}+{1:d}'.format(*layout[window]))

    def run(self) -> None:
        '''
        Run main GUI loop.
        '''

        self.gui_app.mainloop()

    def quit(self) -> None:
        '''
        Quit program.
        '''

        window_layout.save(self._window_layout())
        for window in self.windows:
            self.windows[window].withdraw()
        self.gui_app.quit()

    def _restart(self) -> None:
        '''
        Restart GUI.
        '''

        self.restart.set()
        self.quit()

    def _prepare_windows(self) -> None:
        '''
        Preload windows without displaying them.

        I don't really want to deal with the hassle of non-existing
        windows/trackers, so I do this.
        '''

        prepwindows = []
        for window in self.windows:
            if self.windows[window] is None:
                prepwindows.append(window)
        for window in prepwindows:
            self.commands[window]()
        for window in prepwindows:
            self.windows[window].withdraw()

    def _open_window(
            self, window: str,
            creator: typing.Callable[[], tk.Toplevel]) -> None:
        '''
        Open a window.

        Args:
            window: name of existing window object
            creator: window creation routine
        '''

        try:
            self.windows[window].deiconify()
        except (AttributeError, tk.TclError):
            self.windows[window] = creator()
        self.windows[window].protocol(
            'WM_DELETE_WINDOW', self.windows[window].withdraw)

    def _open_items(self) -> None:
        self._open_window(
            'items', lambda: item_gui.ItemWindow(self.item_tracker))

    def _open_config(self) -> None:
        self._open_window('config', lambda: config.ConfigWindow())

    def _open_itemmap(self) -> None:
        self._open_window(
            'itemmap_c',
            lambda: maps.MapDisplay('item_child', self.location_tracker))
        self._open_window(
            'itemmap_a',
            lambda: maps.MapDisplay('item_adult', self.location_tracker))
        self.windows['itemmap_c'].link_buttons(self.windows['itemmap_a'])
        self.windows['itemmap_a'].link_buttons(self.windows['itemmap_c'])

    def _open_skullmap(self) -> None:
        self._open_window(
            'skullmap_c',
            lambda: maps.MapDisplay('skulls_child', self.location_tracker))
        self._open_window(
            'skullmap_a',
            lambda: maps.MapDisplay('skulls_adult', self.location_tracker))
        self.windows['skullmap_c'].link_buttons(self.windows['skullmap_a'])
        self.windows['skullmap_a'].link_buttons(self.windows['skullmap_c'])

    def _open_dungeons(self) -> None:
        self._open_window(
            'dungeons',
            lambda: dungeon_gui.DungeonWindow(
                dungeon_tracker.DungeonTracker(self.location_tracker)))

    def _open_hints(self) -> None:
        self._open_window('hints', lambda: hints.HintDisplay())

    def _window_layout(self) -> dict:
        '''
        Return current position of all windows.

        Returns:
            dict: {window name: (x, y)}
        '''

        layout = {}
        for window in self.windows:
            if self.windows[window].state() == 'withdrawn':
                continue
            try:
                self.windows[window].deiconify()
            except (AttributeError, tk.TclError):
                continue
            layout[window] = tuple(
                int(c) for c in re.match(
                    '(\d+)x(\d+)([-+]\d+)([-+]\d+)',
                    self.windows[window].geometry()).groups()[2:])
        return layout

    def _reset_items(self) -> None:
        '''
        Reset all items to default.
        '''

        check = tkmbox.askokcancel(
            'Reset', 'This will delete all stored progress.',
            default=tkmbox.CANCEL, icon=tkmbox.WARNING)
        if not check:
            return
        
        storage.delete_autosave()
        for win in self.windows:
            try:
                self.windows[win].reset()
            except AttributeError:
                pass

    def _save(self, path: str = None) -> None:
        '''
        Save state.

        Args:
            path: optional filename; if given, won't ask user for one
        '''

        if not path:
            path = filedialog.asksaveasfilename(defaultextension='.json')
        if path:
            storage.save_autosave(path)

    def _load(self) -> None:
        '''
        Load state.
        '''

        path = filedialog.askopenfilename(defaultextension='.json')
        if path:
            storage.restore_autosave(path)
            self.restart.set()
            self.quit()
