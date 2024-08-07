"""
   usage: python3 HETATM_to_ATOM.py
      1. [path file to pdb file]
      2. [optional: path file to edited pdb]
"""

import sys

# command line inputs
input_file = sys.argv[1]
if len(sys.argv) == 3:
    edited_file = sys.argv[2]
else:
    edited_file = "edited_pdb_file.pdb"

output_file = open(edited_file, "w")
with open(input_file) as pdb:
    for line in pdb:
        line_split = line.split()
        if line_split[0] == "HETATM":
            output_file.write(line.replace("HETATM", "ATOM  "))
