'''
Interface to configuration system.
'''

import json
import os
import sys
import typing

from ..version import __version__ as version

from .default import DEFAULT, OVERWRITE


__all__ = 'Config',


class _c(dict):
    '''
    Single entry info for configuration file.

    Instance variables:
        name: name of the config option
        valtype: type of the config option
        default: default value
    '''

    def __init__(
            self, name: str,
            valtype: typing.Callable[[typing.Any], typing.Any],
            default: typing.Any):
        '''
        Args:
            name: name of the config option
            valtype: type of the config option
            default: default value
        '''

        super().__init__()
        self.name = name
        self.valtype = valtype
        self.default = default


class Config(dict):
    '''
    Program configuration.

    Instance variables:
        filename: full path to config filename
        scheme: config file layout
        _changed: True if config has changed and should be saved
    '''

    def __init__(self):
        super().__init__()

        self._get_scheme()
        self.filename = _config_filename()

        try:
            fid = open(self.filename, 'r')
        except FileNotFoundError:
            imported = None
        else:
            imported = fid.read()

        try:
            imp_dict = {} if imported is None else json.loads(imported)
        except json.decoder.JSONDecodeError:
            imp_dict = {}

        self._changed = False
        for entry in imp_dict:
            self._insert_entry(entry, imp_dict[entry])
        self._check_missing()

        self.set('version', version)
        self.__setitem__ = self._change_entry

    def _get_scheme(self) -> None:
        '''
        Get config file info.

        Writes:
            scheme
        '''

        self.scheme = {}
        for entry in DEFAULT:
            self.scheme[entry[0]] = _c(*entry)

    def _insert_entry(self, entry_name: str, entry_value: typing.Any) -> None:
        '''
        Insert imported entry.

        Args:
            entry: config file entry read from file
        Reads:
            scheme
        Writes:
            self
        '''

        try:
            scheme = self.scheme[entry_name]
        except KeyError:
            self._changed = True
            return

        self[scheme.name] = scheme.valtype(entry_value)

    def _check_missing(self) -> None:
        '''
        Insert missing entries into configuration.

        Reads:
            scheme
        Writes:
            self
        '''

        if 'version' not in self or self['version'] != version:
            for entry in OVERWRITE[version]:
                print(entry)
                self[entry] = self.scheme[entry].default
                self._changed = True
        for entry in self.scheme:
            if entry not in self:
                self[entry] = self.scheme[entry].default
                self._changed = True

    def _string(self) -> str:
        '''
        Convert config into JSON string.

        Reads:
            self
        Returns:
            str: JSON string
        '''

        return json.dumps(dict(self))       

    def _write_to_file(self) -> None:
        '''
        Write config to file if there are any changes.
        '''

        if self._changed:
            with open(self.filename, 'w') as fid:
                fid.write(self._string())
        self._changed = False

    def _change_entry(self, key, value) -> None:
        '''
        Replacement for __setitem__() once config file has been loaded.
        '''

        super().__setitem__(key, value)
        self._changed = True
        self._write_to_file()

    def set(self, key, value) -> None:
        '''
        Set dict item.

        For some reason, _change_entry() doesn't overload __setitem__().
        '''

        self[key] = value
        self._changed = True
        self._write_to_file()


def config_directory() -> str:
    '''
    Return configuration directory.

    This will create said directory if it doesn't exist.

    Returns:
        str: full path to configuration directory
    '''

    if sys.platform.startswith('win32'):
        configdir = os.path.join(os.getenv('LOCALAPPDATA'), 'z5-tracker')
    else:
        configdir = os.path.expanduser('~/.z5-tracker')
    if not os.path.isdir(configdir):
        os.mkdir(configdir)
    return configdir


def _config_filename() -> str:
    '''
    Return config file name.

    This will create the config directory if it doesn't exist. The config file
    itself, however, might not exist.

    Returns:
        str: fill path to config file
    '''

    return os.path.join(config_directory(), 'config.json')
