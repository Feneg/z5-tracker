'''
Default scheme for configuration file.
'''

from ..version import __version__ as version

__all__ = 'DEFAULT', 'OVERWRITE'


DEFAULT = (
    ('autosave', str, 'autosave.json'),
    ('grey_overworld', bool, False),
    ('gui', str, 'gui-tkinter'),
    ('icon_size', float, 1),
    ('layout', str, 'order.conf'),
    ('map_size', float, 1),
    ('ruleset', str, 'rando_aa_v5'),
    ('rule_string', str, 'AJBNNNEA3MAAYAAAAAJC2SWAA'),
    ('show_disabled', bool, False),
    ('show_visible', bool, False),
    ('show_cows', bool, False),
    ('show_scrubs', bool, False),
    ('show_shops', bool, False),
    ('version', str, version),
    ('window_layout', str, 'windows.json'),
)


OVERWRITE = {
    '1.0.0': set(),
    '1.1.0': {'ruleset', 'rule_string'},
    '1.1.1': set(),
    '1.2.0': set(),
    '1.2.1': set()}
