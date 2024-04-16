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

output_folder = "../fold_tree/fromseq"
os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(output_folder, "identifiers.txt")

with open(output_file, 'w') as f:
    for identifier in identifiers:
        f.write(identifier + '\n')

print("Identifiers written to:", output_file)

##COPY IDENTIFIERS.TXT TO RESULTS 
import shutil

source = "../fold_tree/fromseq/identifiers.txt"
destination = "../protostructs/results/identifiers_seq.txt"

try:
    shutil.copy(source, destination)
    print("identifiers copied to results folder")
except OSError as e:
    print("Error", e)

