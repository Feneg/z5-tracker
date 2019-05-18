'''
Map display
'''

import operator
import tkinter as tk
import tkinter.ttk as ttk
import typing

from ..config import CONFIG
from ..config import layout as storage
from ..dungeons.lists import INFO as DUNGEONLOCATIONS
from ..items import image
from ..maps import ITEMLOCATIONS, SKULLTULALOCATIONS
from ..maps.info import MAPSCALE, MAPSPEC, BUTTONTYPE
from .. import world

from . import misc

__all__ = 'MapDisplay',


class MapDisplay(tk.Toplevel):
    '''
    Map window

    Instance variables:
        identifier: map name
        spec: map properties
        scale: map size
        buttons: item location buttons
        links: linked maps
        tracker: location tracker
        available: location availability
        parent: overworld map display (if applicable)
        childmaps: dungeon specific maps tied to this overworld map
    '''

    def __init__(self, spec: str, tracker: world.LocationTracker,
                 parent = None):
        '''
        Args:
            spec: type of map to be crated
            tracker: location tracker
            parent: optional parent window
        '''

        # General initialisation
        super().__init__()
        self.identifier = spec
        self.spec = MAPSPEC[spec]
        self.scale = CONFIG['map_size']
        self.title(self.spec['title'])
        self.parent = parent

        # Set up bottom text label.
        self.helpertext = tk.StringVar()
        self.helper = ttk.Label(
            self, textvariable=self.helpertext,
            font=('Arial', int(12 * self.scale)))
        self.helper.grid(column=0, row=1, sticky=tk.S)

        # Set map type.
        if (
                self.identifier.endswith('_child') or
                self.identifier.endswith('_adult')):
            mapimage = 'overworld'
        else:
            mapimage = DUNGEONLOCATIONS[self.identifier]['mapimg']

        # Set background image.
        imagefile = tk.PhotoImage(file=image(mapimage)[0], master=self)
        imgdim = (
            imagefile.width() * MAPSCALE * self.scale * self.spec['mapscale'],
            imagefile.height() * MAPSCALE * self.scale * self.spec['mapscale'])
        self.m = tk.Canvas(self, height=imgdim[1], width=imgdim[0])
        self.m.grid(column=0, row=0, sticky=misc.A)
        scaling = MAPSCALE * self.scale * self.spec['mapscale']
        for up in range(1, 1000):
            if not (scaling * up) % 1:
                upscale = int(scaling * up)
                break
        else:
            CONFIG.set('map_size', 1)
            assert False
        downscale = int(upscale // scaling)
        if upscale != 1:
            imagefile = imagefile.zoom(upscale, upscale)
        if downscale != 1:
            imagefile = imagefile.subsample(downscale, downscale)
        self.image = self.m.create_image((0, 0), anchor=tk.NW, image=imagefile)
        self.imagefile = imagefile

        # Set-up location tracker.
        self.tracker = tracker
        self.available = {}

        # Place buttons.
        self.buttons = {}
        for b in ITEMLOCATIONS:
            button = ITEMLOCATIONS[b]
            for m in button['maps']: assert m in MAPSPEC
            if 'restriction' in button:
                if ((button['restriction'] == 'scrubshuffle'
                     and not CONFIG['show_scrubs']) or
                    (button['restriction'] == 'shopsanity'
                     and not CONFIG['show_shops'])):
                    continue
            if spec in button['maps']:
                coord = list(
                    int(c * MAPSCALE * self.scale * self.spec['mapscale'])
                    for c in button['coordinates'])
                coord.reverse()
                self.add_button(b, coord, button['type'])
        for b in SKULLTULALOCATIONS:
            button = SKULLTULALOCATIONS[b]
            for m in button['maps']:
                assert m in MAPSPEC
            if spec in button['maps']:
                coord = list(
                    int(c * MAPSCALE * self.scale * self.spec['mapscale'])
                    for c in button['coordinates'])
                coord.reverse()
                self.add_button(b, coord, button['type'])
        for b in DUNGEONLOCATIONS:
            button = DUNGEONLOCATIONS[b]
            if 'maps' not in button:
                continue
            for m in button['maps']: assert m in MAPSPEC
            if 'restriction' in button:
                if ((button['restriction' ]== 'scrubshuffle'
                     and not CONFIG['show_scrubs']) or
                    (button['restriction'] == 'shopsanity'
                     and not CONFIG['show_shops'])):
                    continue
            if spec in button['maps']:
                coord = list(
                    int(c * MAPSCALE * self.scale * self.spec['mapscale'])
                    for c in button['location'])
                coord.reverse()
                self.add_button(b, coord, 'dungeon')

        # Restore latest button states.
        self._restore_autosave()
        self.update_buttons()

        # Prepare for linked maps.
        self.links = {}
        self.childmaps = {}

        # Register this window with location tracker.
        self.tracker.register_gui(self)

    def _update_availability(self) -> None:
        '''
        Update availability database.

        Writes:
            available
        '''

        if self.spec['loctype'] == 'dungeon':
            self.available = self.tracker.check_availability('item')
            self.available.update(self.tracker.check_availability('skulltula'))
        else:
            self.available = self.tracker.check_availability(
                self.spec['loctype'])

    def _set_colour(self, button: str, colour: str, display) -> None:
        '''
        Set button colour.

        Args:
            button: button name
            colour: colour scheme
            display: map display object
        '''

        buttontype = display.buttons[button]['type']
        if buttontype == 'dungeon':
            if self.identifier.startswith('skulls_'):
                buttontype = 'spider'
        display.m.itemconfigure(
            display.buttons[button]['id'],
            activefill=BUTTONTYPE[buttontype]['colours'][colour]['active'],
            fill=BUTTONTYPE[buttontype]['colours'][colour]['normal'],
            outline='black', width=1)

    def add_button(
            self, name: str, location: typing.Sequence[int],
            buttontype: str) -> None:
        '''
        Add a button to map.

        Args:
            name: identifier for new button
            location: coordinates for centre of button
            buttontype: type of button
        '''

        if buttontype not in BUTTONTYPE:
            buttontype = 'standard'
        new = BUTTONTYPE[buttontype]['shape'](self, location)
        self.buttons[name] = {
            'id': new, 'type': buttontype, 'state': True, 'links': set()}
        self._set_colour(name, 'on', self)
        if buttontype == 'dungeon':
            self.m.tag_bind(
                new, '<ButtonRelease-1>', lambda _: self._click_dungeon(name))
        else:
            self.m.tag_bind(
                new, '<ButtonRelease-1>', lambda _: self._click_button(name))
            self.m.tag_bind(
                new, '<ButtonRelease-1>', self.autosave, add='+')
            if self.parent is not None:
                self.m.tag_bind(
                    new, '<ButtonRelease-1>', self.parent.update_buttons,
                    add='+')
        self.m.tag_bind(
            new, '<Enter>', lambda _: self.helpertext.set(name))
        self.m.tag_bind(
            new, '<Leave>', lambda _: self.helpertext.set(''))

    def _click_button(self, name: str) -> None:
        '''
        Event on clicking a button.
        
        Args:
            name: name of the clicked-on button
        '''

        self._switch_button(name, self)
        for links in self.buttons[name]['links']:
            self.links[links]._switch_button(name, self.links[links])

    def _click_dungeon(self, name: str) -> None:
        '''
        Event on clicking a dungeon button.

        Args:
            name: name of the clicked-on button
        '''

        try:
            self.childmaps[name].deiconify()
        except (KeyError, tk.TclError):
            self.childmaps[name] = MapDisplay(name, self.tracker, self)

    def _switch_button(self, name: str, mapdisplay):
        '''
        Switch button state.
        
        Args:
            name: name of the button to be switched
            mapdisplay: map button belongs to
        '''

        colours = BUTTONTYPE[self.buttons[name]['type']]['colours']
        new = not mapdisplay.buttons[name]['state']
        if new:
            if self.buttons[name]['type'] == 'dungeon':
                assert False  # Never should be here.
            else:
                nc = self.available[name]
                nc = 'on' if nc else 'unavailable'
            if 'adult' in self.identifier and not self.tracker.is_adult():
                nc = 'unavailable'
            self._set_colour(name, nc, mapdisplay)
        else:
            self._set_colour(name, 'off', mapdisplay)
        mapdisplay.buttons[name]['state'] = new

    def link_buttons(self, other_map) -> None:
        '''
        Link buttons with buttons from different map.

        Linking is one-way. Tha means that to create a two-way link, each object
        needs to run this method.

        Args:
            other_map: map object to link with
        '''

        self.links[other_map.identifier] = other_map
        for button in self.buttons:
            if button in other_map.buttons:
                self.buttons[button]['links'].add(other_map.identifier)

    def update_buttons(self, args = None) -> None:
        '''
        Update availability of locations.
        '''

        mapping = {True: 'on', False: 'unavailable'}
        self._update_availability()
        for button in self.buttons:
            if self.buttons[button]['state']:
                if self.buttons[button]['type'] == 'dungeon':
                    nc = self.update_dungeon(button)
                else:
                    nc = self.available[button]
                    nc = 'on' if nc else 'unavailable'
                if 'adult' in self.identifier and not self.tracker.is_adult():
                    nc = 'unavailable'
                try:
                    self._set_colour(button, nc, self)
                except tk.TclError as err:
                    raise world.DisplayGone() from err

    def update_dungeon(self, dungeonbutton: dict) -> str:
        '''
        Check supposed display state of dungeon button.

        Args:
            dungeonbutton: dungeon location
        Returns:
            str: 'off', 'on', 'partial' or 'unavailable'
        '''

        buttonchildren = self.tracker.dungeon_locations(dungeonbutton)
        buttonchildren = (
            buttonchildren[0] if self.identifier.startswith('item_')
            else buttonchildren[1])
        try:
            childbuttons = self._load_autosave(dungeonbutton)
        except KeyError:
            childbuttons = {}
            for child in buttonchildren:
                childbuttons[child] = True
        finally:
            children = []
            for child in buttonchildren:
                try:
                    if childbuttons[child]:
                        children.append(self.available[child])
                except KeyError:
                    pass
            if not children:
                nc = 'off'
            elif all(children):
                nc = 'on'
            elif any(children):
                fullclear = self.tracker.dungeon_availability(
                    dungeonbutton,
                    ('item' if self.identifier.startswith('item_')
                     else 'skulltula'))
                nc = 'on' if fullclear else 'partial'
            else:
                nc = 'unavailable'

        return nc

    def reset(self) -> None:
        '''
        Reset location tracker.
        '''

        for button in self.buttons:
            self.buttons[button]['state'] = True
        self.tracker.reset()
        self.update_buttons()

    def store(self):
        '''
        Return location states for storage.

        Returns:
            dict: list of item locations and their state
        '''

        states = {}
        for button in self.buttons:
            states[button] = self.buttons[button]['state']
        return states

    def restore(self, states: dict) -> None:
        '''
        Restore location states from storage.

        Args:
            states: list of item locations and their state
        '''

        for button in states:
            try:
                self.buttons[button]['state'] = states[button]
            except KeyError:
                continue
            self._set_colour(button, 'on' if states[button] else 'off', self)

    def autosave(self, args, linked: bool = True) -> None:
        '''
        Autosave location states.

        Args:
            link: if True, also store linked map
        '''

        storage.autosave('Maps,{0:s}'.format(self.identifier), self)
        if linked:
            for link in self.links:
                self.links[link].autosave(None, False)

    def _restore_autosave(self) -> None:
        '''
        Restore autosave location states.
        '''

        try:
            self.restore(self._load_autosave(self.identifier))
        except KeyError:
            self.restore({})

    def _load_autosave(self, mapid: str) -> dict:
        '''
        Load autosave file.
        
        Args:
            mapid: map identifier
        Returns:
            dict: autsave file contents
        '''

        return storage.load_save()['Maps,{0:s}'.format(mapid)]

    def _standard_icon(self, location: typing.Sequence[int]) -> int:
        '''Rectangular symbol'''
        shape = -20, -20, 20, 20
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_rectangle(*loc)
        return new

    def _enemy_icon(self, location: typing.Sequence[int]) -> int:
        '''Enemy symbol'''
        shape = -20, 0, 10, 15, 20, 0, 10, -15
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_polygon(*loc)
        return new

    def _npc_icon(self, location: typing.Sequence[int]) -> int:
        '''NPC symbol'''
        shape = -20, 20, 0, -20, 20, 20
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_polygon(*loc)
        return new

    def _shop_icon(self, location: typing.Sequence[int]) -> int:
        '''Shop symbol'''
        shape = -15, -20, 15, 20
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_oval(*loc)
        return new

    def _song_icon(self, location: typing.Sequence[int]) -> int:
        '''Song symbol'''
        shape = -20, -15, 20, 15
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_oval(*loc)
        return new

    def _free_icon(self, location: typing.Sequence[int]) -> int:
        '''Free symbol'''
        shape = 0, -20, 20, 0, 0, 20, -20, 0
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_polygon(*loc)
        return new

    def _heart_icon(self, location: typing.Sequence[int]) -> int:
        '''Heart symbol'''
        shape = (0, -10, 15, -20, 20, -15, 10, 15,
                 0, 20, -10, 15, -20, -15, -15, -20, 0, -10)
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_polygon(*loc, smooth=1)
        return new

    def _fairy_icon(self, location: typing.Sequence[int]) -> int:
        '''Fairy symbol'''
        shape = (0, -20, 10, -20, 20, 10, 20, 20, 10, 20, 0, 10,
                 -10, 20, -20, 20, -20, 10, -10, -20)
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_polygon(*loc, smooth=1)
        return new

    def _sub_icon(self, location: typing.Sequence[int]) -> int:
        '''Subterranean symbol'''
        shape = -20, -20, 0, 20, 20, -20
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_polygon(*loc)
        return new

    def _stone_icon(self, location: typing.Sequence[int]) -> int:
        '''Gossip stone symbol'''
        shape = 0, -20, 20, -10, 0, 20, -20, -10
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_polygon(*loc)
        return new

    def _dungeon_icon(self, location: typing.Sequence[int]) -> int:
        '''Dungeon symbol'''
        shape = -30, -30, 30, 30
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_rectangle(*loc)
        return new

    def _ganon_icon(self, location: typing.Sequence[int]) -> int:
        '''Go-mode symbol'''
        shape = (0, -40, 9, -10, 40, -10, 15, 9, 24, 40, 0, 21,
                 -24, 40, -15, 9, -40, -10, -9, -10)
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_polygon(*loc)
        return new

    def _night_icon(self, location: typing.Sequence[int]) -> int:
        '''Night skulltula symbol'''
        shape = -20, -20, -10, -20, 20, 0, -10, 20, -20, 20
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_polygon(*loc)
        return new

    def _high_icon(self, location: typing.Sequence[int]) -> int:
        '''High skulltula symbol'''
        shape = 0, -20, 20, 10, 20, 20, -20, 20, -20, 10
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_polygon(*loc)
        return new

    def _bean_icon(self, location: typing.Sequence[int]) -> int:
        '''Bean skulltula symbol'''
        shape = -20, -20, -20, -10, 0, 20, 20, -10, 20, -20
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_polygon(*loc)
        return new

    def _tree_icon(self, location: typing.Sequence[int]) -> int:
        '''Bean patch symbol'''
        shape = 20, -20, 10, -20, -20, 0, 10, 20, 20, 20
        loc = _make_symbol_coordinates(location, shape, self.spec['mapscale'])
        new = self.m.create_polygon(*loc)
        return new


def _make_symbol_coordinates(
        location: typing.Sequence[int], shape: typing.Sequence[int],
        mapscale: float) -> list:
    '''
    Create corner points for map symbol.

    Args:
        location: centre of symbol
        shape: symbol corners relative to centre point
        mapscale: additional map scaling factor
    Returns:
        list: flat list of coordinates for symbol creation
    '''

    loc = list(location[:2]) * (len(shape) // 2)
    scaled = tuple(int(c * MAPSCALE * CONFIG.get('map_size')) for c in shape)
    loc = [loc[l] + scaled[l] for l in range(len(scaled))]
    return loc

