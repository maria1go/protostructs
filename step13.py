#MSA visualization of seq+str

import numpy as np
from matplotlib import pyplot as plt


#1)
def read_fasta(filename: str) -> tuple[list[str], list[str]]:
    with open(filename, 'r') as f:
        raw = f.read().split('>')[1:]
    ids, sequences = [], []
    for row in raw:
        i, seq = row.split('\n', 1)
        i = i.split(' ')[0]
        ids.append(i)
        seq = seq.replace('\n', '')
        sequences.append(seq)
    return ids, sequences


def get_aa_mapping() -> dict:
    mapping = {v: i for i, v in enumerate('ACDEFGHIKLMNPQRSTVWYBZX')}
    mapping['-'] = -1
    return mapping


def sequences_to_ints(sequences: list[str], mapping: dict) -> np.ndarray:
    arr = np.array([list(x) for x in sequences])
    return np.array([[mapping.get(y) for y in x] for x in arr])    


def get_coverage_matrix(matrix: np.ndarray, gap_int: int) -> np.ndarray:    
    seqid = (np.array(matrix[0] == matrix).mean(-1))
    seqid_sort = seqid.argsort()
    non_gaps = (matrix != gap_int).astype(float)
    non_gaps[non_gaps == 0] = np.nan
    return non_gaps[seqid_sort] * seqid[seqid_sort, None]


def plot_coverage(matrix: np.ndarray, cov_matrix: np.ndarray, gap_int: int, 
                  curve_color: str, curve_width: float, curve_alpha: float, figsize: tuple[int, int],
                  savename: str = None) -> None:
    plt.figure(figsize=figsize, dpi=100)
    plt.title("Sequence coverage")
    plt.imshow(cov_matrix,
               interpolation='nearest', aspect='auto',
               cmap="rainbow_r", vmin=0, vmax=1, origin='lower')
    plt.plot((matrix != gap_int).sum(0), color=curve_color, lw=curve_width, alpha=curve_alpha)
    plt.xlim(-0.5, cov_matrix.shape[1] - 0.5)
    plt.ylim(-0.5, cov_matrix.shape[0] - 0.5)
    plt.colorbar(label="Sequence identity to query", pad=0.02)
    plt.xlabel("Positions")
    plt.ylabel("Sequences")
    plt.tight_layout()
    if savename is not None:
        plt.savefig(savename, bbox_inches='tight')
    plt.show()

#2

def plot_msa_coverage(filename: str, mapping: dict = None,
                      figsize: tuple[int, int] = (15, 4), 
                      curve_color: str = 'k', curve_width: float = 1., curve_alpha: float = 1.,                      
                      savename: str = None) -> None:
    ids, sequences = read_fasta(filename)

    if mapping is None:
        mapping = get_aa_mapping()

    matrix = sequences_to_ints(sequences, mapping)
    cov_matrix = get_coverage_matrix(matrix, gap_int=mapping['-'])
    plot_coverage(matrix, cov_matrix, figsize=figsize, curve_width=curve_width, curve_alpha=curve_alpha,
                  curve_color=curve_color, gap_int=mapping['-'], savename=savename)


filename = 'results/combined.msa.fasta'
plot_msa_coverage(filename, figsize=(30, 5),savename='results/combined_alignment_coverage.png', curve_alpha=0.5)
