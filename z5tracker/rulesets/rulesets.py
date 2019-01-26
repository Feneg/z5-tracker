'''
Rulesets importer.
'''

import importlib

from ..config import CONFIG

rules = importlib.import_module(
    '.{0:s}'.format(CONFIG['ruleset']), package=__package__)

Ruleset = rules.Ruleset

__all__ = 'Ruleset',
