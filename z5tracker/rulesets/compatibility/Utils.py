'''
Library providing functions stubs for compatibility with rulesets
'''

import os
from random import choices as random_choices

__all__ = 'random_choices', 'local_path'

local_path = os.getcwd()
