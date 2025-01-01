#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  write.py
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


class Write():
    """Reading Settings Object"""
    def __init__(self, settings_dir: str, auto_save=True):
        self._commands_file = f"{settings_dir}/launch_commands.json"
        self._settings_file = f"{settings_dir}/settings.json"
        self.auto_save = auto_save

        self._commands = {}
        self._settings = {}

    def _read_settings(self) -> dict:
        """Read in a file for editing"""
        with open(self._settings_file, "r") as file:
            return json.load(file)

    def _read_commands(self) -> dict:
        """Read in a file for editing"""
        with open(self._commands_file, "r") as file:
            return json.load(file)

    def _write_settings(self):
        """Read in a file for editing"""
        with open(self._settings_file, "w+") as file:
            json.dump(self._settings, file, indent=2)

    def _write_commands(self):
        """Read in a file for editing"""
        with open(self._commands_file, "w+") as file:
            json.dump(self._commands, file, indent=2)

    def set_command(self, command_class: str, command_type: str, command: list) -> bool:
        """Set a given command to run a given program"""
        commands = self._read_commands()
        if command_class == "window_manager":
            if command_type not in commands[command_class]:
                raise KeyError(f"{command_type} not valid for {command_class}")
            commands[command_class][command_type]["command"] = command
            if self.auto_save:
                self._write_commands()
            return True
        if command_type not in commands[command_class]:
            raise KeyError(f"{command_type} not valid for {command_class}")
        commands[command_class][command_type] = command
        if self.auto_save:
            self._write_commands()
        return True

    def set_setting(self, key: str, value) -> bool:
        """Set a given setting"""
        settings = self._read_settings()
        if key not in settings:
            raise KeyError(f"{key} not a valid setting.")
        if isinstance(value, type(settings[key])):
            raise TypeError(f"{type(value)} not a valid type for {key}. Type must be: {type(settings[key])}")
        if key in ("window_manager", "steam_type"):
            # only certain settings are valid here. We have to do this error
            # checking ourselves.
            commands = self._read_commands()
            if value not in commands[key]:
                raise ValueError(f"{value} not valid for {key}. Value must be one of: {", ".join(list(commands[key].keys()))}")
