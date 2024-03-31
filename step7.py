##Preparing .fasta files and identifiers.txt


#Extracting identifiers, identifiers+sequences from Foldseek output, writing seq + str .fasta
#1) Identifiers are used in FoldTree for obtaining .pdb structures
#2) identifiers+sequences (str) are written to .fasta file for MSA and visualization
#3) 2 .fasta files are combined for MSA of proteins found both by sequence-based + structure-based approaches.
#####!seq.fasta is not appended to str.fasta directly since it was filtered by HHfilter after MSA! 
#####The ids are mapped between filtered.msa. and seq.fasta, and only seqs of proteins present in filtered.msa are appended to combined file.

m8_file = "pipeline/alis_afdb-swissprot.m8"
output_file = "identifiers.txt"
fasta_file = "str_alignment.fasta"
output_folder = "fold_tree/fromstr"
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
        else:
            seq += line.strip()
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


#FILTERING

filtered_ids = set()
with open("msa.filtered.fasta", 'r') as filtered_file:
    for line in filtered_file:
        if line.startswith(">"):
            filtered_ids.add(line.strip().split('.')[0][1:])
print(filtered_ids)



identifiers_aln = []
sequences_aln = []

with open("alignment.fasta", "r") as aln:
    id_aln = ""
    seq_aln = ""
    for line in aln:
        if line.startswith(">"):
            if id_aln and seq_aln:
                sequences_aln.append(seq_aln)
            id_aln = line.strip().split('.')[0][1:]
            seq_aln = ""
            identifiers_aln.append(id_aln)
        else:
            seq_aln += line.strip()


with open("filtered.alignment.fasta", 'w') as content_fasta:
    for id_aln, seq_aln in zip (identifiers_aln, sequences_aln):
        if id_aln in filtered_ids:
            content_fasta.write(">" + id_aln + "\n" + seq_aln + "\n")

print("Written to filtered.alignment.fasta")

##PREVIOUS VERSION - UNFILTERED SEQUENCES FROM ALIGNMENT.FASTA WERE ALL WRITTEN TO THE NEW FILE


#FASTA COMBINED

with open("filtered.alignment.fasta", 'r') as fasta, open(fasta_file, 'r') as fasta2:
    fasta1_seq = fasta.read()
    fasta2_seq = fasta2.read()

combined_seq = fasta1_seq + '\n' + fasta2_seq

with open(combined_file, 'w') as output:
    output.write(combined_seq)

print('FASTA files combined')

