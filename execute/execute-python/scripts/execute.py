#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Pythia task to execute a Python code
# Author: Sébastien Combéfis <sebastien@combefis.be>
#
# Copyright (C) 2019, Computer Science and IT in Education ASBL
# Copyright (C) 2019, ECAM Brussels Engineering School
#
# This program is free software: you can redistribute it and/or modify
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License, or
#  (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import os
import stat
import subprocess
import sys

PERMISSIONS = stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO

# Setup working directory
workdir = '/tmp/work'
if not os.path.exists(workdir):
    os.makedirs(workdir)
os.chmod(workdir, PERMISSIONS)

# Read input data
data = sys.stdin.read().rstrip('\0')

# Create Python script file
scriptfile = '/tmp/work/program.py'
with open(scriptfile, 'w', encoding='utf-8') as file:
    file.write(data)
os.chmod(scriptfile, PERMISSIONS)

# Execute program.py
proc = subprocess.run(['/usr/bin/python3', '/tmp/work/program.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result = {
    'returncode': proc.returncode,
    'stdout': proc.stdout.decode('utf-8'),
    'stderr': proc.stderr.decode('utf-8')
}
print(json.dumps(result))
