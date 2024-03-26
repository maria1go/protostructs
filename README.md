## External dependencies.
This pipeline depends on the following external programs:
- MAFFT (version ...)
- HHfilter (version ...)
- FoldTree

## 
1. Install MAFFT 

```
sudo apt install mafft

```
2. Install HHfilter 
Download hhfilter.1.gz from: https://manpages.ubuntu.com/manpages/jammy/man1/hhfilter.1.html

```
gzip -d hhfilter.1.gz

```
3. Install FoldTree.
Instructions are available: https://github.com/DessimozLab/fold_tree

! Creating a separate environment is not necessary. Just clone the repo.

! In fold_tree directory, set up 2 folders for the pipeline:
```
mkdir fromseq

mkdir fromstr

```
 
##Workflow

run step1.py entering either protein Uniprot ID or the sequence:

```
python3 step1.py --protein_id {ID}

-OR-

python3 step1.py --sequence {SEQUENCE}

```
