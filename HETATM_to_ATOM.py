"""
   usage: python3 HETATM_to_ATOM.py
      1. [path file to pdb file]
      2. [path file to fixed pdb]
"""

import sys

# command line inputs
input_file = sys.argv[1]
fixed_file = sys.argv[2]

output_file = open(fixed_file, "w")
with open(input_file) as pdb:
    for line in pdb:
        line_split = line.split()
        if line_split[0] == "HETATM":
            output_file.write(line.replace("HETATM", "ATOM  "))
