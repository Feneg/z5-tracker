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

    # Start GUI.
    gui.GUI = gui.guilib.GraphicalInterface()

    # Run program.
    restart = True
    while restart:
        restart = False
        gui.GUI.run()
        if gui.GUI.restart.is_set():
            gui.GUI.restart.clear()
            gui.GUI.gui_root.destroy()
            gui.GUI = gui.guilib.GraphicalInterface()
            restart = True
