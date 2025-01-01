#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  read.py
#
#  Copyright 2025 Thomas Castleman <batcastle@draugeros.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import json


class Read():
    """Reading Settings Object"""
    def __init__(self, settings_dir: str):
        self._commands_file = "f{settings_dir}/launch_commands.json"
        self._settings_file = "f{settings_dir}/settings.json"

        self.settings = {}
        self.commands = {}

        self.reload_settings()

    def get_command(self, command_class: str, command: str) -> list:
        """Return a command value requested by user"""
        # We explicitly do not do any error checking here because if
        # the key does not exist, it will raise a KeyError, which the user can
        # then use for error handling.
        if command_class == "window_manager":
            return self.commands[command_class][command]["command"]
        return self.commands[command_class][command]

    def get_settings(self, key: str):
        """Return a settings value requested by user"""
        # We explicitly do not do any error checking here because if
        # the key does not exist, it will raise a KeyError, which the user can
        # then use for error handling.
        return self.settings[key]

    def reload_settings(self) -> bool:
        """Reload settings from disk"""
        with open(self._commands_file, "r") as file:
            self.commands = json.load(file)

        with open(self._settings_file, "r") as file:
            self.settings = json.load(file)

        return True

    def get_settings_keys(self):
        """Provide settings keys"""
        return self.settings.keys()

    def get_command_keys(self):
        """Provide command keys"""
        return self.commands.keys()

    def get_subkeys(self, key: str, s_or_c=True):
        if s_or_c:
            try:
                return self.settings[key].keys()
            except AttributeError:
                return
        try:
            return self.commands[key].keys()
        except AttributeError:
            return
