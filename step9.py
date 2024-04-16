import subprocess

input_file = "results/str_alignment.fasta"
output_file = "results/str_msa.fasta"

def align_sequences(input_file, output_file):
    mafft_command = f"/mafft --auto --reorder {input_file} > {output_file}"
    subprocess.call(mafft_command, shell=True)

def main():
    align_sequences("results/str_alignment.fasta", "results/str_msa.fasta")
    print("MSA completed.", output_file)


if __name__=="__main__":
    main()



