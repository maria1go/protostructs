This pipeline builds a dataset of relevant protein structures starting from a single sequence using power of both sequence- and structure-based protein alignments.

## External dependencies
This pipeline depends on the following external programs:
- MAFFT (v7.490)
- HHfilter (3.3.0)
- FoldTree

## Workflow
1. Install [MAFFT](https://mafft.cbrc.jp/alignment/software/).

2. Install HH-suite for HHfilter:

```
apt install hhsuite

```
3. Clone [FoldTree](https://github.com/DessimozLab/fold_tree).

! Creating a separate environment is not necessary. Just clone the repo.

! In fold_tree directory, set up 2 folders for the pipeline:
```
mkdir fromseq fromstr

```

4. Install requirements:

```
pip install -r REQUIREMENTS.txt
```

5. Run step1.py entering either protein Uniprot ID or the sequence:

```
python3 step1.py --protein_id {ID}

-OR-

python3 step1.py --sequence {SEQUENCE}

```
## Result
Two sets of relevant protein structures in .pdb format: one sequence-based, and  another structure-based. 

Files:
1. alignment.fasta - homology search result (BLAST)
2. msa.fasta - MSA of BLAST homologs (MAFFT)
3. msa.filtered.fasta - filtered MSA (HHfilter)
4. #identifiers.txt - list of protein identifiers 
5. seq (folder) - .pdb files of seq-aligned proteins found by FoldTree
6. {ticket_name}.tar.gz - Foldseek output
7. alis_afdb-swissprot.m8 - exctracted file from Foldseek output with structural alignment information
8. str_alignment.fasta - protein identifiers with corresponding sequences from .m8 file
9. str_msa.fasta - MSA of protein sequences obtained from structural alignment (MAFFT)
10. str (folder) - .pdb files of str-aligned proteins found by FoldTree
10. combined.fasta - sequences of proteins found via homology search by sequence (and further filtered) + sequences of proteins found by structural alignment combined in one file
11. combined.msa.fasta - MSA of all found protein sequenes altogether
12. seq_alignment_coverage.png - MSA coverage visualisation for proteins obtained by sequence-based approach 
13. str_alignment_coverage.png - MSA coverage visualisation for proteins obtained by structure-based approach 
14. combined_alignment_coverage.png - MSA coverage visualisation for both sets of proteins combined

