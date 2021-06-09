DNA_TO_RNA = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}


def to_rna(dna_strand):
    rna_strand = ""
    for nucleotide in dna_strand:
        rna_strand += DNA_TO_RNA[nucleotide]
    return rna_strand
