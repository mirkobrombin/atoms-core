# proot.py
#
# Copyright 2022 mirkobrombin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundationat version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import shutil
import subprocess

from atoms_core.utils.command import CommandUtils
from atoms_core.exceptions.common import AtomsNoBinaryFound


class ProotWrapper:

    def __init__(self):
        self.__binary_path = self.__find_binary_path()
    
    def __find_binary_path(self) -> str:
        return CommandUtils.which("proot")
    
    def get_proot_command_for_chroot(
        self, 
        chroot_path: str, 
        command: list = None, 
        working_directory: str = None
    ) -> list:
        if command is None:
            command = []

        if working_directory is None:
            working_directory = "/"
        
        command = [
            ("env", "ext_bin"),
            "-i", "HOME=/root", "HOSTNAME=atom", "TERM=xterm",
            self.__binary_path,
            "-w", working_directory,
            # "-b", f"/run/user/{os.getuid()}",  # xorg experiments
            "-S", chroot_path
        ] + command

        return CommandUtils.get_valid_command(command)
    
