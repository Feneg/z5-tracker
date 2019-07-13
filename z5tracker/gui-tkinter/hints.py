'''
Hint display
'''

import operator
import tkinter as tk
import tkinter.ttk as ttk
import typing

from ..config import CONFIG
from ..config import layout as storage
from .. import hints
from .. import rulesets

from . import misc

MAXWOTH = 5
MAXROWS = 34

__all__ = 'HintDisplay',


def _font(size: str = 'normal') -> tuple:
    '''
    Return scaled font.

    Returns:
        tuple: tkinter font variable
    '''

    if size == 'small':
        return ('Arial', int(8 * CONFIG['icon_size']))
    return ('Arial', int(12 * CONFIG['icon_size']))


class HintDisplay(tk.Toplevel):
    '''
    Hints window

    Instance variables:
        rule: item location rules
        regions: list of regions in the game
        items: list of items
        locations: list of potential hint locations
        dungeon: name of dungeons
        obligatory: list of locations with guaranteed hint
        loc_fields: location hint entries
        woth_fields: way of the hero entries
    '''

    def __init__(self):
        super().__init__()
        self.title('Hints')

        self.rules = rulesets.Ruleset()

        regions = [
            [r, r.replace('outside ', '').replace('the ', '')]
            for r in self.rules.list_regions() if isinstance(r, str)]
        regions.sort(key=operator.itemgetter(1))
        self.regions = [r[0] for r in regions]
        self.regions.insert(0, '')
        allitems = self.rules.get_hint_items('all')
        progression = list(hints.HINTITEMS)
        progression.sort()
        items = [allitems[itm][1].replace('the ', '') for itm in progression]
        items.insert(0, '<unimportant>')
        items.insert(0, '<heart piece>')
        items.insert(0, '<rupees>')
        items.insert(0, '<ammo>')
        items.insert(0, '')
        self.items = items
        songs = self.rules.get_hint_items('song')
        songs.sort(key=operator.attrgetter('name'))
        self.songs = [loc.name for loc in songs]
        self.songs.insert(0, '<song>')
        minigame = self.rules.get_hint_items('minigame')
        minigame.sort(key=operator.attrgetter('name'))
        self.minigame = [loc.name for loc in minigame]
        self.minigame.insert(0, '<minigame>')
        overworld = self.rules.get_hint_items('overworld')
        overworld.sort(key=operator.attrgetter('name'))
        self.overworld = [loc.name for loc in overworld]
        self.overworld.insert(0, '<overworld>')
        dungeons = self.rules.get_hint_items('dungeon')
        dungeons.sort(key=operator.attrgetter('name'))
        self.dungeons = [dgn.name for dgn in dungeons]
        self.dungeons.insert(0, '<dungeon>')
        obligatory = self.rules.get_hint_items('always')
        obligatory.sort(key=operator.attrgetter('name'))
        self.obligatory = obligatory

        style = ttk.Style()
        style.configure('hintdisplay.TButton', font=_font(), width=2)
        style.map(
            'hintdisplay.TButton', background=[('alternate', 'green')])
        style.configure('hintdisplay.TMenubutton', font=_font())
        style.map(
            'hintdisplay.TMenubutton', foreground=[('disabled', 'grey')])
        style.configure('hintdisplay.const.TMenubutton', font=_font())
        style.map(
            'hintdisplay.const.TMenubutton',
            foreground=[('disabled', '!alternate', 'black'),
                        ('disabled', 'alternate', 'grey')])
        style.configure('hintdisplay.TLabel', font=_font())
        style.map(
            'hintdisplay.TButton', foreground=[('disabled', 'grey')])

        self.topframe = ttk.Frame(self)
        self.topframe.grid(sticky=misc.A)

        self.wothframe = ttk.Frame(self.topframe)
        self.wothframe.grid(column=0, row=0, sticky=tk.N + tk.W)
        self._build_woth()

        self.locframe = ttk.Frame(self.topframe)
        self.locframe.grid(column=0, row=1, sticky=tk.S + tk.E + tk.W)
        self._build_loc()

        self.restore()

        self._set_autosave()

    def _build_woth(self) -> None:
        '''
        Make 'Way of the Hero' GUI.
        '''

        self.wothlabel = ttk.Label(
            self.wothframe, font=_font(), text='Way of the Hero')
        self.wothlabel.grid(column=0, row=0, sticky=tk.N)

        self.woth_fields = {}
        for row in range(1, MAXWOTH):
            self.woth_fields[row] = WothEntry(
                row, self.wothframe, self._autosave, self.regions)

    def _build_loc(self) -> None:
        '''
        Make generic location hint GUI.
        '''

        self.loclabel = ttk.Label(
            self.locframe, font=_font(), text='Location hints')
        self.loclabel.grid(column=0, row=0, sticky=tk.N)

        reference = len(self.obligatory) + 1
        hintset = self.rules.get_hint_distribution()
        dist = {'songs': (
            reference + 2 if hintset in ('balanced', 'strong') else
            reference + 1)}
        dist['minigame'] = (
            dist['songs'] + 2 if hintset in ('balanced', 'strong') else
            dist['songs'] + 0 if hintset == 'tournament' else
            dist['songs'] + 1)
        dist['overworld'] = (
            dist['minigame'] + 2 if hintset == 'tournament' else
            dist['minigame'] + 4)
        dist['dungeons'] = (
            dist['overworld'] + 3 if hintset == 'tournament' else
            dist['overworld'] + 4)

        self.loc_fields = {}
        for row in range(1, reference):
            self.loc_fields[row] = LocEntry(
                row, self.locframe, self._autosave, self.items, self.regions,
                self.obligatory[row - 1].name)
        for row in range(reference, MAXROWS):
            for htype in dist:
                if row < dist[htype]:
                    break
            else:
                htype = 'regions'
            self.loc_fields[row] = LocEntry(
                row, self.locframe, self._autosave, self.items,
                getattr(self, htype))

    def restore(self) -> None:
        '''
        Restore data from save.
        '''

        try:
            data = storage.load_save()['Hints']
        except KeyError:
            return
        if not data:
            return
        for row in range(1, MAXWOTH):
            self.woth_fields[row].variable.set(data['woth'][row - 1][1])
            if data['woth'][row - 1][0]:
                self.woth_fields[row].okpress()
        for row in range(1, len(self.obligatory) + 1):
            self.loc_fields[row].itemvar.set(data['loc'][row - 1][1])
        for row in range(len(self.obligatory) + 1, MAXROWS):
            try:
                self.loc_fields[row].itemvar.set(data['loc'][row - 1][1])
                self.loc_fields[row].locvar.set(data['loc'][row - 1][2])
            except IndexError:
                break
        for row in range(1, MAXROWS):
            try:
                if data['loc'][row - 1][0]:
                    self.loc_fields[row].okpress()
            except IndexError:
                break
        self._autosave()

    def entry_data(self) -> dict:
        '''
        Return all currently set data.

        Returns:
            dict: {woth: list of tuples, loc: list of tuples}
        '''

        ret = {}
        ret['woth'] = []
        for row in range(1, MAXWOTH):
            ret['woth'].append(
                (self.woth_fields[row].statetrack.get(),
                 self.woth_fields[row].variable.get()))
        ret['loc'] = []
        for row in range(1, MAXROWS):
            ret['loc'].append(
                (self.loc_fields[row].statetrack.get(),
                 self.loc_fields[row].itemvar.get(),
                 self.loc_fields[row].locvar.get()))
        return ret

    def _autosave(self, *args) -> None:
        '''
        Autosave
        '''

        storage.autosave('Hints', hints.HintTracker(self.entry_data()))

    def _set_autosave(self):
        '''
        Establish autosaving.
        '''

        for row in range(1, MAXWOTH):
            self.woth_fields[row].variable.trace('w', self._autosave)
        for row in range(1, MAXROWS):
            self.loc_fields[row].itemvar.trace('w', self._autosave)
            self.loc_fields[row].locvar.trace('w', self._autosave)

    def reset(self):
        '''
        Reset to default state.
        '''

        for row in range(1, MAXWOTH):
            self.woth_fields[row].delpress()
        for row in range(1, MAXROWS):
            self.loc_fields[row].delpress()


class LocEntry(ttk.Frame):
    '''
    Entry in location hint GUI.

    Instance variables:
        autosave: function for autosaving
        default: default location string
        itemvar: currently chosen item
        itemmenu: item menu object
        locvar: currently chosen location
        locmenu: location menu object
        obligatory: True of this hint is a guaranteed location
    '''

    def __init__(self, row: int, parent: ttk.Frame, autosave,
                 items: typing.Sequence, regions: typing.Sequence,
                 obligatory: str = None,):
        '''
        Args:
            row: row placement in parent widget
            parent: parent widget
            items: list of possible items with hints
            regions: list of location names pointed at by generic hints
            obligatory: if set, this entry will be a guaranteed hint
        '''

        super().__init__(parent)

        itemvar = tk.StringVar()
        itemmenu = ttk.OptionMenu(
            self, itemvar, *items, style='hintdisplay.TMenubutton')
        itemmenu.config(width=18)
        itemmenu.nametowidget(itemmenu.cget('menu')).config(font=_font('small'))
        itemmenu.grid(column=0, row=0, sticky=misc.A)

        locvar = tk.StringVar()
        if not obligatory:
            locmenu = ttk.OptionMenu(
                self, locvar, *regions, style='hintdisplay.TMenubutton')
            locmenu.config(width=22)
            locmenu.nametowidget(locmenu.cget('menu')).config(font=_font())
        else:
            locmenu = ttk.OptionMenu(
                self, locvar, style='hintdisplay.const.TMenubutton')
            locmenu.config(width=22)
            locmenu.state(('disabled',))
            locvar.set(obligatory)
        locmenu.grid(column=1, row=0, sticky=misc.A)

        okbutton = ttk.Button(
            self, command=self.okpress, text='✔', style='hintdisplay.TButton')
        okbutton.grid(column=2, row=0)
        statetrack = tk.BooleanVar()
        statetrack.set(False)
        delbutton = ttk.Button(
            self, command=self.delpress, text='❌',
            style='hintdisplay.TButton')
        delbutton.grid(column=3, row=0)

        self.grid(column=0, row=row, sticky=tk.E + tk.W)

        self.autosave = autosave
        self.default = regions[0]
        self.itemvar = itemvar
        self.itemmenu = itemmenu
        self.locvar = locvar
        self.locmenu = locmenu
        self.obligatory = bool(obligatory)
        self.okbutton = okbutton
        self.statetrack = statetrack
        self.delbutton = delbutton
        
    def okpress(self, force_enable: bool = False) -> None:
        '''
        OK button press.
        '''

        if self.itemmenu.instate(('disabled',)) or force_enable:
            self.itemmenu.state(('!disabled',))
            if self.obligatory:
                self.locmenu.state(('!alternate',))
            else:
                self.locmenu.state(('!disabled',))
            self.okbutton.state(('!alternate',))
            self.statetrack.set(False)
        else:
            self.itemmenu.state(('disabled',))
            if self.obligatory:
                self.locmenu.state(('alternate',))
            else:
                self.locmenu.state(('disabled',))
            self.okbutton.state(('alternate',))
            self.statetrack.set(True)
        self.autosave()

    def delpress(self) -> None:
        '''
        Reset button press.
        '''

        self.itemvar.set('')
        if not self.obligatory:
            self.locvar.set(self.default)
        self.okpress(True)
            

class WothEntry(ttk.Frame):
    '''
    Entry in 'Way of the Hero' GUI.

    Instance variables:
        autosave: function for autosaving
        variable: currently chosen region
        menu: menu object
        okbutton: mark button
        delbutton: reset button
    '''

    def __init__(self, row: int, parent: ttk.Frame, autosave,
                 regions: typing.Sequence):
        '''
        Args:
            row: row placement in parent widget
            parent: parent widget
            regions: list of region names
            autosave: autosave function
        '''

        super().__init__(parent)

        variable = tk.StringVar()
        menu = ttk.OptionMenu(
            self, variable, *regions, style='hintdisplay.TMenubutton')
        menu.config(width=20)
        menu.nametowidget(menu.cget('menu')).config(font=_font())
        menu.grid(column=0, row=0, sticky=misc.A)

        okbutton = ttk.Button(
            self, command=self.okpress, text='✔', style='hintdisplay.TButton')
        okbutton.grid(column=1, row=0)
        statetrack = tk.BooleanVar()
        statetrack.set(False)
        delbutton = ttk.Button(
            self, command=self.delpress, text='❌',
            style='hintdisplay.TButton')
        delbutton.grid(column=2, row=0)

        self.grid(column=0, row=row, sticky=tk.E + tk.W)

        self.autosave = autosave
        self.variable = variable
        self.menu = menu
        self.okbutton = okbutton
        self.statetrack = statetrack
        self.delbutton = delbutton
        
    def okpress(self, force_enable: bool = False) -> None:
        '''
        OK button press.
        '''

        if self.menu.instate(('disabled',)) or force_enable:
            self.menu.state(('!disabled',))
            self.okbutton.state(('!alternate',))
            self.statetrack.set(False)
        else:
            self.menu.state(('disabled',))
            self.okbutton.state(('alternate',))
            self.statetrack.set(True)
        self.autosave()

    def delpress(self) -> None:
        '''
        Reset button press.
        '''

        self.variable.set('')
        self.okpress(True)
