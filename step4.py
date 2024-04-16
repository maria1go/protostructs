import os
import shutil
#Extracting protein identifiers from MSA file


identifiers = []
with open("results/msa.filtered.fasta", 'r') as f:
    for line in f:
        if line.startswith('>'):
            identifier = line.strip().split('.')[0][1:]
            identifiers.append(identifier)
            
##TRANSFER IDENTIFIERS TO FOLDTREE

output_folder_name = "fold_tree/fromseq"
output_folder = os.path.join(os.path.expanduser("~"), output_folder_name)  

os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(output_folder, "identifiers.txt")
#output_file = 'identifiers.txt'

with open(output_file, 'w') as f:
    for identifier in identifiers:
        f.write(identifier + '\n')


print("Identifiers written to:", output_file)

##COPY IDENTIFIERS.TXT TO RESULTS 
import shutil

ids_seq_dirname = "fold_tree/fromseq"
ids_seq = os.path.join(os.path.expanduser("~"), ids_seq_dirname)
source = os.path.join(ids_seq, "identifiers.txt")


pipeline_ids_dirname = "protostructs/results/identifiers_seq.txt"
pipeline_ids = os.path.join(os.path.expanduser("~"), pipeline_ids_dirname)
destination = pipeline_ids

try:
    shutil.copy(source, destination)
    print("identifiers copied to results folder")
except OSError as e:
    print("Error", e)
