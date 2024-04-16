import subprocess
import os

# Change to Foldtree directoty 
target_dirname = "fold_tree"
dirname = os.path.join(os.path.expanduser("~"), target_dirname)
os.chdir(dirname)


command = [
    "snakemake",
    "--cores", "4",
    "--use-conda",
    "-s", "./workflow/fold_tree",
    "--config", "folder=./fromstr", "filter=False"
]

# Execute the command
try:
    subprocess.run(command, check=True)
    print("+")
except subprocess.CalledProcessError as e:
    print("Error executing command:", e)

#Copy .structs to the current directory

import shutil

structs_dirname = "fold_tree/fromstr/structs"
structs = os.path.join(os.path.expanduser("~"), structs_dirname)
source = structs

pipeline_dirname = "protostructs/results"
pipeline = os.path.join(os.path.expanduser("~"), pipeline_dirname)
os.chdir(pipeline)
destination = "str"

try:
    shutil.copytree(source, destination)
    print("Results in str folder")
except OSError as e:
    print("Error retrieving results")
