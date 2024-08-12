"""
    Incoporate iodine into model. YOU HAVE TO GO INTO
    DS VISUALIZER TO REMOVE THE BOND.

   usage: python3 make_one_model.py
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

atom_serial_num = 0
output_file     = open(edited_file, "w+")
with open(input_file) as pdb:
    for line in pdb:
        line_split = line.split()
        if (line_split[0] != "MODEL") & (line_split[0] != "ENDMDL") & (line_split[0] != "REMARK"):
            if (line_split[0] == "HETATM") or (line_split[0] == "ATOM"):
                atom_serial_num += 1
                if 'I' in line_split[2]:
                    list_line            = list(line)
                    atom_serial_num_char = str(atom_serial_num)
                    list_line[6:11]      = atom_serial_num_char.rjust(5)
                    new_line             = "".join(list_line)
                    output_file.write(new_line)
                    continue
            output_file.write(line)

