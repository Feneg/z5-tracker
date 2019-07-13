'''
Explain colour coding of map locations.
'''

import tkinter as tk
import tkinter.ttk as ttk

from ..config import CONFIG
from ..maps.info import BUTTONTYPE

from . import misc

__all__ = 'HelpWindow',


class HelpWindow(tk.Toplevel):
    '''
    Colour help window.
    '''

    def __init__(self):
        super().__init__()
        self.title('Help')

        self.topframe = ttk.Frame(self)
        self.topframe.grid(sticky=misc.A)

        self.itemframe = ttk.LabelFrame(self, text='Items')
        self.itemframe.grid(column=0, row=0, sticky=tk.W + tk.N + tk.S)
        itementries = [('on', 'Available'), ('off', 'Already checked'),
                       ('unavailable', 'Unavailable')]
        if CONFIG['show_visible']:
            itementries.append(('visible', 'Visible but unavailable'))
        self._add_listing(self.itemframe, 'standard', itementries)
        self.itemdframe = ttk.LabelFrame(
            self.itemframe, text='Dungeon summary')
        self.itemdframe.grid(
            column=0, row=len(itementries), columnspan=2,
            sticky=tk.W + tk.E + tk.S)
        itemdentries = (('on', 'All available'), ('off', 'Fully cleared'),
                        ('unavailable', 'Nothing logically available'),
                        ('partial', 'At least partially available'))
        self._add_listing(self.itemdframe, 'dungeon', itemdentries)

        self.spiderframe = ttk.LabelFrame(self, text='Skulltulas')
        self.spiderframe.grid(column=1, row=0, sticky=tk.N + tk.S)
        spiderentries = (('on', 'Available'), ('off', 'Already collected'),
                         ('unavailable', 'Unavailable'))
        self._add_listing(self.spiderframe, 'spider', spiderentries)
        self.spiderdframe = ttk.LabelFrame(
            self.spiderframe, text='Dungeon summary')
        self.spiderdframe.grid(
            column=0, row=len(spiderentries), columnspan=2,
            sticky=tk.W + tk.E + tk.S)
        spiderdentries = (('on', 'All available'), ('off', 'All collected'),
                          ('unavailable', 'None logically available'),
                          ('partial', 'At least some available'))
        self._add_listing(self.spiderdframe, 'spider', spiderdentries)

        self.stoneframe = ttk.LabelFrame(self, text='Gossip Stones')
        self.stoneframe.grid(column=2, row=0, sticky=tk.E + tk.N + tk.S)
        stoneentries = (('on', 'Available'), ('off', 'Already checked'),
                        ('unavailable', 'Unavailable'))
        self._add_listing(self.stoneframe, 'stone', stoneentries)

    def _add_listing(
            self, pframe: ttk.LabelFrame, ctype: str, entries: tuple) -> None:
        '''
        Make colour list.

        Args:
            pframe: parent frame
            ctype: 'standard'
            entries: list of (state, description)
        '''

        row = 0
        for state, text in entries:
            button = tk.Canvas(
                pframe,
                background=BUTTONTYPE[ctype]['colours'][state]['normal'],
                height=25, width=25)
            button.grid(column=0, row=row, sticky=tk.W)
            text = ttk.Label(pframe, text=text)
            text.grid(column=1, row=row, sticky=tk.W)
            row += 1
