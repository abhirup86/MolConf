from imports_and_setup import *
from conformer_generation_visualization import *

def copy_paste_filea_to_b(file1, file2, start_line, end_line):
    with open(file1, 'r') as f1:
        lines = f1.readlines()

    start_line -= 1
    end_line -= 1

    segment = lines[start_line:end_line+1]

    with open(file2, 'a') as f2:
        for line in segment:
            f2.write(line)

import subprocess

def run_xtb_gfn2_optimization():
    # call your bash script here
    subprocess.run(["bash ./xtb.sh"], shell=True)

def run_xtb_gfn2_optimization_with_solvent():
    # call your bash script here with added arguments for solvent
    subprocess.run(["bash xtb_solvent.sh", "solvent_arguments"], shell=True)
