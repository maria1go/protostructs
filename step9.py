import subprocess

input_file = "str_alignment.fasta"
output_file = "str_msa.fasta"

def align_sequences(input_file, output_file):
    mafft_command = f"/mafft --auto --reorder {input_file} > {output_file}"
    subprocess.call(mafft_command, shell=True)

def main():
    align_sequences("str_alignment.fasta", "str_msa.fasta")
    print("MSA completed.", output_file)

if __name__=="__main__":
    main()



