import subprocess
import os 
#
# Change to the desired directory
dirname = "/home/vmadmin/fold_tree"
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


###Enter .structs folder and copy to output folder?

