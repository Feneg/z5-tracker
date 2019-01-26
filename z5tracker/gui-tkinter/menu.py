'''
Main control window.
'''

import tkinter as tk
import tkinter.ttk as ttk
import typing

from . import misc

__all__ = 'MenuWindow',


class MenuWindow(tk.Toplevel):
    '''
    Main control window.
    '''

    def __init__(self, commands: typing.Dict[str, typing.Callable[[], None]]):
        '''
        Args:
            commands: set of functions for the buttons
        '''

        super().__init__()
        self.title('Menu')

        self.frame = ttk.Frame(self)
        self.frame.grid(sticky=misc.A)

        self.buttons = {
            'items': self._make_button((0, 0), commands['items'], 'Items'),
            'dungeons': self._make_button(
                (1, 0), commands['dungeons'], 'Dungeons'),
            'itemmap': self._make_button(
                (0, 1), commands['itemmap'], 'Item Map'),
            'skullmap': self._make_button(
                (1, 1), commands['skullmap'], 'Skulltula Map'),
            'hints': self._make_button((1, 2), commands['hints'], 'Hints'),
            'config': self._make_button((0, 3), commands['config'], 'Options'),
            'load': self._make_button((0, 4), commands['load'], 'Load'),
            'save': self._make_button((1, 4), commands['save'], 'Save'),
            'quit': self._make_button((0, 5), commands['quit'], 'Quit'),
            'reset': self._make_button((1, 5), commands['itemreset'], 'Reset'),
            }

    def _make_button(
            self, loc: typing.Sequence[int],
            action: typing.Callable[[], None],
            text: str or tk.StringVar) -> ttk.Button:
        '''
        Shortcut to place buttons.

        Args:
            loc: (column, row) of button on 2D grid
            action: function to call when button is pressed

        Returns:
            ttk.Button: created button
        '''

        button = ttk.Button(self.frame, command=action)
        if isinstance(text, tk.StringVar):
            button.configure(textvariable=text)
        else:
            assert isinstance(text, str)
            button.configure(text=text)
        button.grid(column=loc[0], row=loc[1], sticky=tk.N+tk.W+tk.E)
        return button
