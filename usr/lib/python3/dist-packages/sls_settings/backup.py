#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  backup.py
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
import os


class BackUp():
    """Backup functions"""
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        self.file_path = file_path

    def check_if_backedup(self) -> bool:
        """Check if original settings are backed up"""
        if os.path.exists(f"{self.file_path}.bak"):
            if self.is_backup_same():
                return True
        return False

    def is_backup_same(self) -> bool:
        """Check if Backup file and currently in use file are the same"""
        if self.check_if_backedup():
            with open(self.file_path, "rb+") as file:
                current_file = file.read()
            with open(f"{self.file_path}.bak", "rb+") as file:
                og_file = file.read()
            if og_file == current_file:
                return True
        return False

    def back_up(self) -> bool:
        """Backup current file"""
        if self.is_backup_same():
            return True
        self._clear_backup()
        with open(f"{self.file_path}.bak", "wb+") as file1:
            with open(self.file_path, "rb+") as file2:
                file1.write(file2.read())
        return True

    def _clear_backup(self) -> bool:
        """Delete current backup file"""
        try:
            os.remove(f"{self.file_path}.bak")
        except FileNotFoundError:
            pass
        except PermissionError:
            return False
        return True

    def restore_backup(self) -> bool:
        """Restore the current backup to operational status"""
        if self.is_backup_same():
            return False
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass
        with open(f"{self.file_path}.bak", "rb+") as file2:
            with open(self.file_path, "wb+") as file1:
                file1.write(file2.read())
