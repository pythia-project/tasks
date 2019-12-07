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
input = json.loads(data)

# Create Python script file
scriptfile = '/tmp/work/program.py'
with open(scriptfile, 'w', encoding='utf-8') as file:
    file.write(input['header'] + '\n' + input['code'])
os.chmod(scriptfile, PERMISSIONS)

# Execute program.py for each test case
results = []
outputs = []
for i in range(len(input['inputs'])):
    proc = subprocess.run(['/usr/bin/python3', '/tmp/work/program.py'], input=input['inputs'][i], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Check execution error
    if proc.returncode != 0:
        print(json.dumps({'tid': input['tid'], 'status': 'error', 'message': proc.stderr}))
        sys.exit(0)
    # Check result
    outputs.append(proc.stdout)
    results.append(outputs[-1] == input['outputs'][i])

# Generate output
success = sum(results)
output = {'tid': input['tid'], 'status': 'success' if success == len(input['inputs']) else 'failed', 'outputs': {'actual': outputs}, 'valid': results}
if 'mirror' in input and input['mirror']:
    output['inputs'] = input['inputs']
    output['outputs']['expected'] = input['outputs']
print(json.dumps(output))
