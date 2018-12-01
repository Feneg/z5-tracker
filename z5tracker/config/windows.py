'''
Window layout configuration.
'''

import json
import os.path

from .__init__ import CONFIG
from .config import config_directory

__all__ = 'load', 'save'


def load() -> dict:
    '''
    Load window layout info.

    Returns:
        layout: window layout following format {window name: (x, y)}
    '''

    try:
        fid = open(
            os.path.join(config_directory(), CONFIG['window_layout']), 'r')
    except FileNotFoundError:
        layout = {}
    else:
        try:
            layout = json.load(fid)
        except json.JSONDecodeError:
            layout = {}
        finally:
            fid.close()
    return layout


def save(layout: dict) -> None:
    '''
    Save window layout to file.

    Returns:
        layout: window layout following format {window name: (x, y)}
    '''

    with open(os.path.join(config_directory(), CONFIG['window_layout']),
              'w') as fid:
        json.dump(layout, fid)
