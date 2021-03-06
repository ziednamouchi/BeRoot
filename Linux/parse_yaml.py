#!/usr/bin/env python
import os
import json
import yaml # install pyyaml if needed

"""
Get a dictionary from yaml files
- git clone https://github.com/GTFOBins/GTFOBins.github.io/
- parse.py should be at the root directory of GTFOBins

This script should help me to update easily my binary list here: 
- https://github.com/AlessandroZ/BeRoot/blob/master/Linux/beroot/analyse/binaries.py
"""

results = {}
root = '_gtfobins'
for file in os.listdir(root):
    if file.endswith('.md'):
        with open(os.path.join(root, file), 'r') as stream:
            binary = os.path.splitext(file)[0]
            results[binary] = {}
            gtfo_bins = yaml.load_all(stream)
            for gtfo_bin in gtfo_bins:
                if gtfo_bin:
                    functions = gtfo_bin['functions']
                    # Sorted by priority
                    for func in ['execute-interactive', 'execute-non-interactive', 'file-write', 'file-read',
                                 'sudo-enabled', 'download', 'upload']:
                        if func in functions:
                            results[binary] = functions[func][0]['code']
                            break

json_parsed = json.dumps(results, indent=4, sort_keys=True)
print(json_parsed)
