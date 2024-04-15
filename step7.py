##Preparing .fasta files and identifiers.txt


#Extracting identifiers, identifiers+sequences from Foldseek output, writing seq + str .fasta
#1) Identifiers are used in FoldTree for obtaining .pdb structures
#2) identifiers+sequences (str) are written to .fasta file for MSA and visualization
#3) 2 .fasta files are combined for MSA of proteins found both by sequence-based + structure-based approaches.
#####!seq.fasta is not appended to str.fasta directly since it was filtered by HHfilter after MSA! 
#####The ids are mapped between filtered.msa. and seq.fasta, and only seqs of proteins present in filtered.msa are appended to combined file.
import os

pipeline_dirname = "protostructs/results"
pipeline = os.path.join(os.path.expanduser("~"), pipeline_dirname)

m8_file = os.path.join(pipeline,"alis_afdb-swissprot.m8")
output_file = os.path.join(pipeline,"identifiers.txt")
fasta_file = os.path.join(pipeline, "str_alignment.fasta")
combined_file = os.path.join(pipeline,"combined.fasta")

str_dirname = "fold_tree/fromstr"
str = os.path.join(os.path.expanduser("~"), str_dirname)
output_folder = str 

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

##TRANSFER IDENTIFIERS TO FOLDTREE
import os

os.makedirs(output_folder, exist_ok=True)
output_file2 = os.path.join(output_folder, "identifiers.txt")

with open(output_file2, 'w') as f:
    for identifier in identifiers:
        f.write(identifier + '\n')


print("Identifiers written to the foldtree directory.")

##COPY IDENTIFIERS TO RESULTS
import shutil

ids_seq_dirname = "fold_tree/fromstr"
ids_seq = os.path.join(os.path.expanduser("~"), ids_seq_dirname)
source = os.path.join(ids_seq, "identifiers.txt")


pipeline_ids_dirname = "protostructs/results/identifiers_str.txt"
pipeline_ids = os.path.join(os.path.expanduser("~"), pipeline_ids_dirname)
destination = pipeline_ids

try:
    shutil.copy(source, destination)
    print("identifiers copied to results folder")
except OSError as e:
    print("Error", e)

#FILTERING

filtered_ids = set()
with open("results/msa.filtered.fasta", 'r') as filtered_file:
    for line in filtered_file:
        if line.startswith(">"):
            filtered_ids.add(line.strip().split('.')[0][1:])
print(filtered_ids)

identifiers_aln = []
sequences_aln = []

with open("results/alignment.fasta", "r") as aln:
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


with open("results/filtered.alignment.fasta", 'w') as content_fasta:
    for id_aln, seq_aln in zip (identifiers_aln, sequences_aln):
        if id_aln in filtered_ids:
            content_fasta.write(">" + id_aln + "\n" + seq_aln + "\n")

print("Written to filtered.alignment.fasta")

#FASTA COMBINED

with open("results/filtered.alignment.fasta", 'r') as fasta, open(fasta_file, 'r') as fasta2:
    fasta1_seq = fasta.read()
    fasta2_seq = fasta2.read()

combined_seq = fasta1_seq + '\n' + fasta2_seq

with open(combined_file, 'w') as output:
    output.write(combined_seq)

print('FASTA files combined')

