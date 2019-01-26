'''
Location map for Zelda 5.
'''

import importlib

from .config import CONFIG
from . import gui

__all__ = 'main',


def main() -> None:
    '''
    Main program.
    '''

    # Run program.
    restart = True
    while restart:
        gui.GUI = gui.guilib.GraphicalInterface()
        restart = False
        gui.GUI.run()
        if gui.GUI.restart.is_set():
            del gui.GUI
            restart = True
