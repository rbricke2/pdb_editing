"""
    usage: python3 C2_prime_endo_and_C3_prime_endo.py
        1. [path file to C2' endo conformation pdb file]
        2. [path file to C3' endo conformation pdb file]
        3. [optional: path file to combined pdb]
"""

import sys

# command line inputs
C2endo_file = sys.argv[1]
C3endo_file = sys.argv[2]
if len(sys.argv) == 4:
    combined_file = sys.argv[3]
else:
    combined_file = "C2endo_and_C3endo.pdb"

def get_lines(file):
    lines = []
    with open(file) as pdb:
        for line in pdb:
            line_split = line.split()
            if (line_split[0] == "HETATM") or (line_split[0] == "ATOM"):
                if 'HO' not in line_split[2]:
                    lines.append(line)
                else: # 'HO5 -> H5T and 'H03 -> H3T
                    if line_split[2] == "'HO5":
                        lines.append(line.replace("'HO5", " H5T"))
                    else:
                        lines.append(line.replace("'HO3", " H3T"))
        return lines

def write_lines(output_file, lines):
    for line in lines:
        line_split = line.split()
        if (line_split[0] != "REMARK") & (line_split[0] != "TER"):
            new_line = line
            if line_split[0] == "HETATM":
                new_line = line.replace("HETATM", "ATOM  ")
            if ("H" in line_split[2]) and ("'" in line_split[2]) and (len(line_split[2]) == 4):
                list_line = list(new_line)
                name = list_line[12:16]
                name.append(name.pop(0))
                list_line[12:16] = name
                new_line = "".join(list_line)
            output_file.write(new_line)

# get lines for C2' endo conformation
C2endo = get_lines(C2endo_file)
# get lines for C3' endo conformation
C3endo = get_lines(C3endo_file)

# write new file
with open(combined_file, "w+") as output_file:
    output_file.write("MODEL 1\n")
    write_lines(output_file, C2endo)
    output_file.write("ENDMDL\nMODEL 2\n")
    write_lines(output_file, C3endo)
    output_file.write("ENDMDL\n")