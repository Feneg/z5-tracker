'''
General map properties.
'''

__all__ = 'MAPSCALE', 'MAPSPEC', 'BUTTONTYPE'


MAPSCALE = 0.25

MAPSPEC = {
    'item_child': {
        'title': 'Child Item Map', 'loctype': 'item', 'mapscale': 1},
    'item_adult': {
        'title': 'Adult Item Map', 'loctype': 'item', 'mapscale': 1},
    'skulls_child': {
        'title': 'Child Skulltula Map', 'loctype': 'skulltula', 'mapscale': 1},
    'skulls_adult': {
        'title': 'Adult Skulltula Map', 'loctype': 'skulltula', 'mapscale': 1},
    'skulls_child': {
        'title': 'Child Skultula Map', 'loctype': 'skulltula', 'mapscale': 1},
    'skulls_adult': {
        'title': 'Adult Skultula Map', 'loctype': 'skulltula', 'mapscale': 1},
    'Deku Tree': {
        'title': 'Inside the Deku Tree', 'loctype': 'dungeon', 'mapscale': 1},
    'Dodongos Cavern': {
        'title': "Dodongo's Cavern", 'loctype': 'dungeon', 'mapscale': 1},
    'Jabu Jabus Belly': {
        'title': "Jabu-Jabu's Belly", 'loctype': 'dungeon', 'mapscale': 1},
    'Ice Cavern': {
        'title': 'Ice Cavern', 'loctype': 'dungeon', 'mapscale': 1},
    'Bottom of the Well': {
        'title': 'Bottom of the Well', 'loctype': 'dungeon', 'mapscale': 1},
    'Gerudo Training Grounds': {
        'title': 'Gerudo Training Grounds', 'loctype': 'dungeon',
        'mapscale': 1},
    'Forest Temple': {
        'title': 'Forest Temple', 'loctype': 'dungeon', 'mapscale': 1},
    'Fire Temple': {
        'title': 'Fire Temple', 'loctype': 'dungeon', 'mapscale': 1},
    'Water Temple': {
        'title': 'Water Temple', 'loctype': 'dungeon', 'mapscale': 1},
    'Shadow Temple': {
        'title': 'Shadow Temple', 'loctype': 'dungeon', 'mapscale': 0.5},
    'Spirit Temple': {
        'title': 'Spirit Temple', 'loctype': 'dungeon', 'mapscale': 1},
    'Ganons Castle': {
        'title': "Ganon's Castle", 'loctype': 'dungeon', 'mapscale': 1}
}

BUTTONTYPE = {}
BUTTONTYPE['standard'] = {
    'colours': {
        'on': {'active': '#0f0', 'normal': '#0c0'},
        'off': {'active': '#aaa', 'normal': 'grey'},
        'unavailable': {'active': '#f00', 'normal': '#c00'}
    },
    'shape': lambda self, location: self._standard_icon(location)}
BUTTONTYPE['chest'] = BUTTONTYPE['standard']
BUTTONTYPE['enemy'] = {
    'colours': BUTTONTYPE['standard']['colours'],
    'shape': lambda self, location: self._enemy_icon(location)}
BUTTONTYPE['npc'] = {
    'colours': BUTTONTYPE['standard']['colours'],
    'shape': lambda self, location: self._npc_icon(location)}
BUTTONTYPE['shop'] = {
    'colours': BUTTONTYPE['standard']['colours'],
    'shape': lambda self, location: self._shop_icon(location)}
BUTTONTYPE['song'] = {
    'colours': BUTTONTYPE['standard']['colours'],
    'shape': lambda self, location: self._song_icon(location)}
BUTTONTYPE['free'] = {
    'colours': BUTTONTYPE['standard']['colours'],
    'shape': lambda self, location: self._free_icon(location)}
BUTTONTYPE['heart'] = {
    'colours': BUTTONTYPE['standard']['colours'],
    'shape': lambda self, location: self._heart_icon(location)}
BUTTONTYPE['fairy'] = {
    'colours': BUTTONTYPE['standard']['colours'],
    'shape': lambda self, location: self._fairy_icon(location)}
BUTTONTYPE['sub'] = {
    'colours': BUTTONTYPE['standard']['colours'],
    'shape': lambda self, location: self._sub_icon(location)}
BUTTONTYPE['stone'] = {
    'colours': {
        'on': {'active': '#9aa', 'normal': '#ddd'},
        'off': {'active': '#aaa', 'normal': 'grey'},
        'unavailable': {'active': '#f00', 'normal': '#c00'}},
    'shape': lambda self, location: self._stone_icon(location)}
BUTTONTYPE['dungeon'] = {
    'colours': {
        'on': {'active': '#0f0', 'normal': '#0c0'},
        'off': {'active': '#aaa', 'normal': 'grey'},
        'unavailable': {'active': '#f00', 'normal': '#c00'},
        'partial': {'active': '#ff0', 'normal': '#cc0'}},
    'shape': lambda self, location: self._dungeon_icon(location)}
BUTTONTYPE['ganon'] = {
    'colours': BUTTONTYPE['standard']['colours'],
    'shape': lambda self, location: self._ganon_icon(location)}
BUTTONTYPE['spider'] = {
    'colours': {
        'on': {'active': '#ff0', 'normal': '#f80'},
        'off': {'active': '#aaa', 'normal': 'grey'},
        'unavailable': {'active': '#f0f','normal': '#c0a'},
        'partial': {'active': '#ff0', 'normal': '#cc0'}},
    'shape': lambda self, location: self._standard_icon(location)}
BUTTONTYPE['night'] = {
    'colours': BUTTONTYPE['spider']['colours'],
    'shape': lambda self, location: self._night_icon(location)}
BUTTONTYPE['high'] = {
    'colours': BUTTONTYPE['spider']['colours'],
    'shape': lambda self, location: self._high_icon(location)}
BUTTONTYPE['bean'] = {
    'colours': BUTTONTYPE['spider']['colours'],
    'shape': lambda self, location: self._bean_icon(location)}
BUTTONTYPE['tree'] = {
    'colours': BUTTONTYPE['spider']['colours'],
    'shape': lambda self, location: self._tree_icon(location)}
