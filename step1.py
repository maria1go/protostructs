import argparse
import subprocess
import urllib.request
import urllib.error
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

def protein_sequence(protein_id):
    url = f"https://www.uniprot.org/uniprot/{protein_id}.fasta"
    try:
        with urllib.request.urlopen(url) as response:
            lines = response.read().decode('utf-8').split('\n')
            sequence = "".join(lines[1:])
        return sequence
    except urllib.error.URLError as e:
        print("Error")
        return None

def blast_homology_search(sequence, number_alignments, hitlist):
    result_handle = NCBIWWW.qblast("blastp", "swissprot", sequence, alignments=number_alignments, hitlist_size=hitlist)
    blast_record = NCBIXML.read(result_handle)
    with open("results/alignment.fasta", "w") as output_file:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                output_file.write(">{}\n".format(alignment.title.split('|')[1]))
                output_file.write("{}\n".format(hsp.sbjct))

def main():
    parser = argparse.ArgumentParser(description='Fetch protein sequence from UniProt and perform BLAST homology search')
    parser.add_argument('--protein_id', type=str, help='UniProt protein ID')
    parser.add_argument('--sequence', type=str, help='Manually entered protein sequence')
    parser.add_argument('--alignments', type=int, default=1000, help='Number of alignments in search')
    parser.add_argument('--hitlist', type=int, default=100, help='Number of alignments to return')
    args = parser.parse_args()


#Fetching sequence
    if args.protein_id:
        get_sequence = protein_sequence(args.protein_id)
    elif args.sequence:
        get_sequence = args.sequence
    else:
        print("Please provide either --protein_id or sequence.")
        return
        
    print(f"\n{get_sequence}")

    
#BLAST homology search
    number_alignments = args.alignments
    hitlist = args.hitlist
    
    if get_sequence:
       blast_record = blast_homology_search(get_sequence, number_alignments, hitlist)
 
    print("Homology search completed, results are written to alignment.fasta")

    

    # Step 2 - Run MAFFT
    subprocess.run(["python3", "step2.py"], check=True)

    #Step 3 - HHfilter
    subprocess.run(["python3", "step3.py"], check=True)

    #Step 4 - Extracting protein identifiers
    subprocess.run(["python3", "step4.py"], check=True)

    #Step 5 - Running FoldTree 
    subprocess.run(["python3", "step5.py"], check=True)

    #Step 6 - Fetching .pdb file and Foldseek structural alignment, extracting result from .tar.gz file 
    subprocess.run(["python3", "step6.py"], check=True)
    
    #Step 7 - Extracting sequences and identifiers from Foldseek result
    subprocess.run(["python3", "step7.py"], check=True)

    #Step 8 - Running FoldTree
    subprocess.run(["python3", "step8.py"], check=True)

    #Step 9 - Run MAFFT
    subprocess.run(["python3", "step9.py"], check=True)
 
    #Step 10 -  MSA visualization (3 plots)
    subprocess.run(["python3", "step10.py"], check=True)


if __name__ == "__main__":
    main()


