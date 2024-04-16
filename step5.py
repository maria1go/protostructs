import subprocess
import shutil
import os 

# Changing to the FoldTree directory
target_dirname = "fold_tree"
dirname = os.path.join(os.path.expanduser("~"), target_dirname)
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

structs_dirname = "fold_tree/fromseq/structs"
structs = os.path.join(os.path.expanduser("~"), structs_dirname)
source = structs

pipeline_dirname = "protostructs/results"
pipeline = os.path.join(os.path.expanduser("~"), pipeline_dirname)
os.chdir(pipeline)
destination = "seq"

try:
    shutil.copytree(source, destination)
    print("Results in seq folder")
except OSError as e:
    print("Error retrieving results")
