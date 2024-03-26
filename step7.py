##Preparing .fasta files and identifiers.txt


#Extracting identifiers, identifiers+sequences from Foldseek output, writing seq + str .fasta
#1) Identifiers are used in FoldTree for obtaining .pdb structures
#2) identifiers+sequences are written to .fasta file for MSA and visualization
#3) 2 .fasta files are combined for MSA of proteins found both by sequence-based + structure-based approaches.

m8_file = "/home/vmadmin/pipeline/alis_afdb-swissprot.m8"
output_file = "identifiers.txt"
fasta_file = "str_alignment.fasta"
output_folder = "/home/vmadmin/fold_tree/fromstr"
combined_file = "combined.fasta"

identifiers = []
sequences = []

#Reading query id+sequence since it is absent in .m8 file
with open("alignment.fasta", "r") as f:
    sequence_id = ""
    seq = ""
    for line in f:
        if line.startswith(">"):
            sequence_id = line.strip().split('.')[0][1:]
            identifiers.append(sequence_id)
            break
        else:
            seq = line.strip()
            sequences.append(seq)
            break

#Extracting identifiers and sequences
with open(m8_file, 'r') as f:
    for line in f:
        title = line.strip().split('\t')[1]
        identifier = title.split('-')[1]
        identifiers.append(identifier)
        sequence = line.strip().split('\t')[18]
        sequences.append(sequence)


#Writing to files
with open(output_file, 'w') as f:
    for identifier in identifiers:
        f.write(identifier + '\n')

print("Identifiers written to:", output_file)

with open(fasta_file, 'w') as f:
    for identifier, sequence in  zip (identifiers, sequences):
        f.write(">"+ identifier + '\n' + sequence + '\n')

print("Sequences written to:", fasta_file)

##TRANSFER IDENTIFIERS TO THE RIGHT FOLDER FOR FOLDTREE

import os

#output_folder = "/home/vmadmin/fold_tree/fromstr"

os.makedirs(output_folder, exist_ok=True)

output_file2 = os.path.join(output_folder, "identifiers.txt")


with open(output_file2, 'w') as f:
    for identifier in identifiers:
        f.write(identifier + '\n')


print("Identifiers written to the foldtree directory.")


#FASTA combined
with open("alignment.fasta", 'r') as fasta1, open(fasta_file, 'r') as fasta2:
    fasta1_seq = fasta1.read()
    fasta2_seq = fasta2.read()

combined_seq = fasta1_seq + '\n' + fasta2_seq

with open(combined_file, 'w') as output:
    output.write(combined_seq)

print('FASTA files combined')
