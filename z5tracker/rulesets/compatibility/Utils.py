'''
Library providing functions stubs for compatibility with rulesets
'''

import os
from random import choices as random_choices

from ...config import CONFIG

__all__ = 'random_choices', 'local_path', 'data_path'

local_path = os.getcwd()


def data_path(subfolder: str) -> str:
    return os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', CONFIG['ruleset'],  'data', subfolder))
