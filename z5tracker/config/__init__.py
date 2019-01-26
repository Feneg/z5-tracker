'''
Program configuration infrastructure.
'''

from . import config
from . import globals

__all__ = 'CONFIG',

globals.CONFIG = config.Config()
CONFIG = globals.CONFIG
