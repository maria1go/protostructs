import subprocess
import os

# Change to Foldtree directoty 
dirname = "../fold_tree"
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


structs = "../fold_tree/fromstr/structs"
source = structs

pipeline = "../protostructs/results"
os.chdir(pipeline)
destination = "str"

try:
    shutil.copytree(source, destination)
    print("Results in str folder")
except OSError as e:
    print("Error retrieving results")
