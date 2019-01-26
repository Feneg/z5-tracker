'''
Configuration for item layout.
'''

import configparser
import json
import os
import typing

from ..version import __version__ as version

from .globals import CONFIG
from . import config

__all__ = ('NoConfig', 'load', 'new', 'autosave', 'save', 'load_save',
           'delete_autosave')


class NoConfig(Exception):
    '''
    Raised when item layout config is not available.
    '''

    pass


def load(ltype: str) -> dict:
    '''
    Load item/dungeon layout.

    Args:
        ltype: 'Items' or 'Dungeons'
    Returns:
        dict: layout in format {identifier: (column, row)}
    Raise:
        NoConfig, configparser.Error: if no item layout is available
    '''
    
    inp = configparser.ConfigParser(allow_no_value=True)
    try:
        fid = open(os.path.join(
            config.config_directory(), CONFIG['layout']), 'r')
    except FileNotFoundError as err:
        raise NoConfig() from err
    try:
        inp.read_file(fid)
    finally:
        fid.close()
    if ltype not in inp:
        raise NoConfig()
    try:
        if inp['version']['version'] != version:
            raise NoConfig()
    except (KeyError, configparser.NoSectionError,
            configparser.NoOptionError) as err:
        if version != version:
            raise NoConfig() from err

    layout = {}
    for item in inp[ltype]:
        if not inp[ltype][item]:
            continue
        try:
            sep = tuple(int(c) for c in inp[ltype][item].split(','))
        except ValueError as err:
            raise NoConfig() from err
        if len(sep) != 2:
            raise NoConfig()
        layout[item] = sep

    return layout


def new(layouts: typing.Mapping[
        str, typing.Mapping[str, typing.Sequence[int]]]):
    '''
    Create new layout file.

    Args:
        layouts: layout in format {identifier: (column, row)}
    '''

    out = configparser.ConfigParser(allow_no_value=True)

    out.add_section('Items')
    for item in layouts['Items']:
        out['Items'][item] = ', '.join(str(c) for c in layouts['Items'][item])
    out.add_section('Dungeons')
    for dungeon in layouts['Dungeons']:
        out['Dungeons'][dungeon] = ', '.join(
            str(c) for c in layouts['Dungeons'][dungeon])

    with open(os.path.join(
            config.config_directory(), CONFIG['layout']), 'w') as fid:
        out.write(fid)


def autosave(ltype: str, tracker) -> None:
    '''
    Perform autosave.

    Args:
        ltype: 'Items' or 'Dungeons', 'Hints' or starting with 'Maps,'
        tracker: tracker providing info
    '''

    autosavefile = os.path.join(config.config_directory(), CONFIG['autosave'])
    save = load_save()
    save[ltype] = tracker.store()
    save['version'] = version
    with open(autosavefile, 'w') as fid:
        json.dump(save, fid)


def save(trackers: dict, filepath: str) -> None:
    '''
    Save current item setup.

    Args:
        trackers: tracker providing info
        filepath: savefile path
    '''

    to_store = {}
    for dtype in trackers:
        try:
            to_store[dtype] = trackers[dtype].store()
        except AttributeError:
            to_store[dtype] = {}
            for mtype in trackers[dtype].gui:
                to_store[dtype][mtype.identifier] = mtype.store()
    to_store['version'] = version
    with open(filepath, 'w') as fid:
        json.dump(to_store, fid)


def load_save(filepath: str = os.path.join(
        config.config_directory(), CONFIG['autosave'])) -> None or dict:
    '''
    Load save file.

    Args:
        filepath: full path to file to load
    Return:
        dict: save data
    Raises:
        FileNotFoundError: if file doesn't exist (unless it's the autosave)
    '''

    try:
        fid = open(filepath, 'r')
    except FileNotFoundError:
        if filepath == os.path.join(
                config.config_directory(), CONFIG['autosave']):
            return {}
        else:
            raise

    try:
        data = json.load(fid)
    except json.JSONDecodeError:
        data = {}
    finally:
        fid.close()

    try:
        if data['version'] != version:
            data = {}
    except KeyError:
        if version != '1.0.0':
            data = {}

    return data


def delete_autosave() -> None:
    '''
    Delete autosave file.
    '''

    autosavefile = os.path.join(config.config_directory(), CONFIG['autosave'])
    try:
        os.remove(autosavefile)
    except FileNotFoundError:
        pass


def save_autosave(filepath: str) -> None:
    '''
    Copy autosave into dedicated file.

    Args:
        filepath: savefile path
    '''

    autosavefile = os.path.join(config.config_directory(), CONFIG['autosave'])
    with open(autosavefile, 'r') as infid:
        with open(filepath, 'w') as outfid:
            outfid.write(infid.read())


def restore_autosave(filepath: str) -> None:
    '''
    Copy dedicated file into autosave.

    Args:
        filepath: savefile path
    '''

    autosavefile = os.path.join(config.config_directory(), CONFIG['autosave'])
    with open(filepath, 'r') as infid:
        with open(autosavefile, 'w') as outfid:
            outfid.write(infid.read())
