import subprocess
import shutil
import os 

# Changing to the FoldTree directory
dirname = "../fold_tree"
os.chdir(dirname)

command = [
    "snakemake",
    "--cores", "4",
    "--use-conda",
    "-s", "./workflow/fold_tree",
    "--config", "folder=./fromseq", "filter=False"
]

# Execute the command
try:
    subprocess.run(command, check=True)
    print("+")
except subprocess.CalledProcessError as e:
    print("Error executing command:", e)


###Enter .structs folder and copy to output folder
source = "../fold_tree/fromseq/structs"

pipeline = "../protostructs"
os.chdir(pipeline)
destination = "results/seq"

try:
    shutil.copytree(source, destination)
    print("Results in seq folder")
except OSError as e:
    print("Error retrieving results", e)
