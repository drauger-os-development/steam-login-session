#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  __init__.py
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
"""__init__ for sls_settings"""
import os
from sls_settings.read import Read
from sls_settings.write import Write
from sls_settings.backup import BackUp

SETTINGS_DIR = "/etc/steam-login-session/"
if not os.path.exists(SETTINGS_DIR):
    SETTINGS_DIR = "../../etc/steam-login-session/"

Read = Read(SETTINGS_DIR)
Write = Write(SETTINGS_DIR)

BackUp_Settings = BackUp(f"{SETTINGS_DIR}/settings.json")
BackUp_Commands = BackUp(f"{SETTINGS_DIR}/launch_commands.json")
