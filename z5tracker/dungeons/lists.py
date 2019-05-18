'''
Default settings
'''

import collections

__all__ = 'INFO', 'REWARDS', 'IMG'


INFO = {
    'Deku Tree': {
        'name': 'Inside the Deku Tree', 'reward': True, 'icon': 'emerald',
        'location': (860, 2450),
        'maps': ('item_child', 'item_adult', 'skulls_child', 'skulls_adult'),
        'mapimg': 'dungeon_dekutree'},
    'Dodongos Cavern': {
        'name': "Dodongo's Cavern", 'reward': True, 'icon': 'ruby',
        'location': (215, 1616),
        'maps': ('item_child', 'item_adult', 'skulls_child', 'skulls_adult'),
        'mapimg': 'dungeon_dodongos'},
    'Jabu Jabus Belly': {
        'name': "Jabu Jabu's Belly", 'reward': True, 'icon': 'sapphire',
        'location': (310, 2460), 'maps': ('item_child', 'skulls_child'),
        'mapimg': 'dungeon_jabujabu'},
    'Ice Cavern': {
        'name': 'Ice Cavern', 'reward': False, 'icon': 'serenade',
        'location': (242, 2520), 'maps': ('item_adult', 'skulls_adult'),
        'mapimg': 'dungeon_ice'},
    'Bottom of the Well': {
        'name': 'Bottom of the Well', 'reward': False, 'icon': 'lens',
        'location': (300, 1930), 'maps': ('item_child', 'skulls_child'),
        'mapimg': 'dungeon_well'},
    'Gerudo Training Grounds': {
        'name': 'Gerudo Training Grounds', 'reward': False,
        'icon': 'gerudo_symbol_colored',
        'location': (428, 540), 'maps': ('item_adult',),
        'mapimg': 'dungeon_gerudo'},
    'Forest Temple': {
        'name': 'Forest Temple', 'reward': True, 'icon': 'forestmedallion',
        'location': (570, 2140), 'maps': ('item_adult', 'skulls_adult'),
        'mapimg': 'dungeon_forest'},
    'Fire Temple': {
        'name': 'Fire Temple', 'reward': True, 'icon': 'firemedallion',
        'location': (35, 1924), 'maps': ('item_adult', 'skulls_adult'),
        'mapimg': 'dungeon_fire'},
    'Water Temple': {
        'name': 'Water Temple', 'reward': True, 'icon': 'watermedallion',
        'location': (1330, 1020), 'maps': ('item_adult', 'skulls_adult'),
        'mapimg': 'dungeon_water'},
    'Shadow Temple': {
        'name': 'Shadow Temple', 'reward': True, 'icon': 'shadowmedallion',
        'location': (330, 2160), 'maps': ('item_adult', 'skulls_adult'),
        'mapimg': 'dungeon_shadow'},
    'Spirit Temple': {
        'name': 'Spirit Temple', 'reward': True, 'icon': 'spiritmedallion',
        'location': (280, 70),
        'maps': ('item_child', 'item_adult', 'skulls_child', 'skulls_adult'),
        'mapimg': 'dungeon_spirit'},
    'Ganons Castle': {
        'name': "Ganon's Castle", 'reward': False, 'icon': 'lightarrow',
        'location': (170, 1440), 'maps': ('item_adult',),
        'mapimg': 'dungeon_ganon'},
}


REWARDS = collections.OrderedDict((
    ('?', 'unknown'),
    ('Kokiri Emerald', 'emerald'),
    ('Goron Ruby', 'ruby'),
    ('Zora Sapphire', 'sapphire'),
    ('Light Medallion', 'lightmedallion'),
    ('Forest Medallion', 'forestmedallion'),
    ('Fire Medallion', 'firemedallion'),
    ('Water Medallion', 'watermedallion'),
    ('Shadow Medallion', 'shadowmedallion'),
    ('Spirit Medallion', 'spiritmedallion')
))


IMG = {
    'worldmap': 'overworld', 'key': 'smallkey', 'bosskey': 'bosskey',
    'chest_full': 'chest_golden_closed', 'chest_empty': 'chest_golden_open'}
