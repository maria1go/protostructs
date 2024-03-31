import os
#Extracting protein identifiers from MSA file


identifiers = []
with open("msa.filtered.fasta", 'r') as f:
    for line in f:
        if line.startswith('>'):
            identifier = line.strip().split('.')[0][1:]
            identifiers.append(identifier)

##TRANSFER IDENTIFIERS TO RIGHT FOLDERS

#output_folders = ["/home/vmadmin/fold_tree/fromseq", "/home/vmadmin/pipeline"]
output_folder = "fold_tree/fromseq"

os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(output_folder, "identifiers.txt")
#output_file = 'identifiers.txt'

with open(output_file, 'w') as f:
    for identifier in identifiers:
        f.write(identifier + '\n')


print("Identifiers written to:", output_file)
