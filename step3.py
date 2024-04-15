import subprocess

#HHfilter.
#output .fasta required
input_file = "results/msa.fasta"
output_file = "results/msa.filtered.fasta"

def filter_sequences(input_file, output_file):
    hhfilter_command = f"/usr/bin/hhfilter -M first -i {input_file} -o {output_file}"
    subprocess.call(hhfilter_command, shell=True)

def main():
    filter_sequences("results/msa.fasta", "results/msa.filtered.fasta")

if __name__=="__main__":
    main()

print("Filtered.", output_file)
