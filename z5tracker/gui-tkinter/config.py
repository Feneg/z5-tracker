'''
Configuration window.
'''

import operator
import tkinter as tk
import tkinter.ttk as ttk
import typing

from ..config import CONFIG

from . import misc

__all__ = 'ConfigWindow',


class ConfigWindow(tk.Toplevel):
    '''
    Config option window.
    '''

    def __init__(self):
        super().__init__()
        self.title('Configuration')

        self.configvalues = {}

        self.frame = ttk.Frame(self)
        self.frame.grid(sticky=misc.A)

        self._display(1,'Autosave', CONFIG['autosave'])
        self._float(2, 'Icon size', 'icon_size')
        self._display(3, 'Item layout', CONFIG['layout'])
        self._float(4, 'Map size', 'map_size')
        self._display(5, 'Ruleset', CONFIG['ruleset'])
        self._string(6, 'Rules string', 'rule_string', _validate_rule_string)
        self._checkbox(7, 'Show disabled locations', 'show_disabled')
        self._checkbox(8, 'Show all scrubs', 'show_scrubs')
        self._checkbox(9, 'Show shops', 'show_shops')
        self._display(10, 'Window Layout', CONFIG['window_layout'])

    def _display(self, row: int, name: str, value: str) -> None:
        '''
        Non-editable string display

        Args:
            row: row placement
            name: name of option
            value: current value of option
        '''

        left = ttk.Label(self.frame, text=name)
        left.grid(column=0, padx=6, pady=3, row=row, sticky=tk.W)
        right = ttk.Entry(self.frame)
        right.insert(0, value)
        right.configure(state='readonly')
        right.grid(column=1, padx=6, pady=3, row=row, sticky=tk.W+tk.E)

    def _string(self, row: int, name: str, configname: str,
                validation: typing.Callable[[str], bool]) -> None:
        '''
        Editable string display

        Args:
            row: row placement
            name: displayed name of option
            configname: name of option in config file
            validation: function used to valied user-entered content
        '''

        left = ttk.Label(self.frame, text=name)
        left.grid(column=0, padx=6, pady=3, row=row, sticky=tk.W)
        self.configvalues[configname] = tk.StringVar()
        self.configvalues[configname].set(CONFIG[configname].upper())
        validater = (self.register(validation), '%P')
        right = ttk.Entry(
            self.frame, validate='all', validatecommand=validater,
            textvariable=self.configvalues[configname], width=40)
        right.grid(column=1, padx=6, pady=3, row=row, sticky=tk.W+tk.E)

    def _float(self, row: int, name: str, configname: str) -> None:
        '''
        Editable float display

        Args:
            row: row placement
            name: displayed name of option
            configname: name of option in config file
        '''

        left = ttk.Label(self.frame, text=name)
        left.grid(column=0, padx=6, pady=3, row=row, sticky=tk.W)
        self.configvalues[configname] = tk.StringVar()
        self.configvalues[configname].set(str(CONFIG[configname]))
        validater = (self.register(_validate_float), configname, '%P')
        right = ttk.Entry(
            self.frame, validate='all', validatecommand=validater,
            textvariable=self.configvalues[configname], width=40)
        right.grid(column=1, padx=6, pady=3, row=row, sticky=tk.W+tk.E)

    def _checkbox(self, row: int, name: str, configname: str) -> None:
        '''
        Checkbox

        Args:
            row: row placement
            name: displayed name of option
            configname: name of option in config file
        '''

        left = ttk.Label(self.frame, text=name)
        left.grid(column=0, padx=6, pady=3, row=row, sticky=tk.W)
        self.configvalues[configname] = tk.IntVar()
        try:
            self.configvalues[configname].set(int(CONFIG[configname]))
        except KeyError:
            self.configvalues[configname].set(0)
        right = ttk.Checkbutton(
            self.frame,
            command=lambda: CONFIG.set(
                configname, bool(self.configvalues[configname].get())),
            takefocus=False, variable=self.configvalues[configname])
        right.grid(column=1, padx=6, pady=3, row=row, sticky=tk.W+tk.E)


def _validate_rule_string(newstring: str) -> True:
    '''
    Validate randomiser rules string and store if string is valid.

    Args:
        newstring: new config string
    Returns:
        True: always
    '''

    if newstring.isalnum():
        CONFIG.set('rule_string', newstring)
    return True


def _validate_float(configname: str, newfloat: str) -> bool:
    '''
    Validate randomiser rules string and store if string is valid float.

    Args:
        configname: name of config entry
        newstring: new config string
    Returns:
        True: always
    '''

    try:
        float(newfloat)
    except ValueError:
        return False
    CONFIG.set(configname, float(newfloat))
    return True
