"""
   usage: python3 fix_15_mer_pdb_and_extract_residue.py
      1. [path file to pdb file of 15-mer with modified thymine]
      2. [path file to fixed pdb file of 15-mer with modified thymine]
      3. [path file to pdb file of modified thymine w/ sugar]
"""

import sys

# command line inputs
input_file = sys.argv[1]
fixed_file = sys.argv[2]
mod_file   = sys.argv[3]

# get lines for the modified thymine
modified_T = []
with open(input_file) as pdb:
    for line in pdb:
        line_split = line.split()
        if line_split[0] == "HETATM":
            modified_T.append(line.replace("HETATM", "ATOM  ").replace("UNK     0", "UNK S   8"))
        if len(line_split) == 12:
            if (line_split[4] == "S") & (line_split[5] == "8"):
                modified_T.append(line.replace(" DT", "UNK"))

# get lines for new file
new_pdb = []
with open(input_file) as pdb:
    start_copying = False
    added_thymine = False
    for line in pdb:
        line_split = line.split()
        if line_split[0] != "REMARK":
            if start_copying:
                if (len(line_split) == 12):
                    if (line_split[4] == "S") & (line_split[5] == "8"):
                        if not added_thymine:
                            new_pdb.extend(modified_T)
                            added_thymine = True
                    else:
                        new_pdb.append(line)
                else:
                    new_pdb.append(line)
            elif line_split[0] == "TER":
                if line_split[2] == "UNK":
                    start_copying = True

fixed_file = open(fixed_file, "w")
atom_serial_num = 1
for i in range(len(new_pdb)):
    line = ""
    line_split = new_pdb[i].split()
    if line_split[0] == "ATOM":
        list_line            = list(new_pdb[i])
        atom_serial_num_char = str(atom_serial_num)
        list_line[6:11]      = atom_serial_num_char.rjust(5)
        line                 = "".join(list_line)
        atom_serial_num     += 1
    
    if line_split[0] == "CONECT":
        continue
    elif not line:
        fixed_file.write(new_pdb[i])
    else:
        fixed_file.write(line)

modified_thymine = open(mod_file, "w")
atom_serial_num = 1
for i in range(len(modified_T)):
    line = ""
    line_split = modified_T[i].split()
    if line_split[0] == "ATOM":
        if ('P' in line_split[2]):
            continue # skip phosphate group... PDB FILE WILL BE MISSING HYGROGENS!
        list_line            = list(modified_T[i])
        atom_serial_num_char = str(atom_serial_num)
        list_line[6:11]      = atom_serial_num_char.rjust(5)
        list_line[21:26]     = "1".rjust(5)
        line                 = "".join(list_line)
        atom_serial_num     += 1
    
    if not line:
        modified_thymine.write(modified_T[i])
    else:
        modified_thymine.write(line)