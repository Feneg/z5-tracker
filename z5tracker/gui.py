'''
Access point to program GUI.
'''

import importlib

from .config import CONFIG

guilib = importlib.import_module(
    '.{0:s}'.format(CONFIG['gui']), package=__package__)

__all__ = 'guilib', 'GUI',

GUI = None
