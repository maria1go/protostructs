import subprocess
mafft = "/usr/bin/mafft"

input_file = "results/alignment.fasta"
output_file = "results/msa.fasta"

def align_sequences(input_file, output_file):
    mafft_command = f"/usr/bin/mafft --auto --reorder {input_file} > {output_file}"
    subprocess.call(mafft_command, shell=True)

def main():
    align_sequences("results/alignment.fasta", "results/msa.fasta")

if __name__=="__main__":
    main()

print("MSA completed.", output_file)
