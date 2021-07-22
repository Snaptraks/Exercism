PROTEINS = {
    "Methionine": ["AUG"],
    "Phenylalanine": ["UUU", "UUC"],
    "Leucine": ["UUA", "UUG"],
    "Serine": ["UCU", "UCC", "UCA", "UCG"],
    "Tyrosine": ["UAU", "UAC"],
    "Cysteine": ["UGU", "UGC"],
    "Tryptophan": ["UGG"],
    "STOP": ["UAA", "UAG", "UGA"],
}

CODONS = {c: protein for protein, codons in PROTEINS.items() for c in codons}


def proteins(strand):
    protein_list = []
    for i in range(len(strand) // 3):
        codon = strand[3 * i: 3 * (i + 1)]
        try:
            protein = CODONS[codon]
        except KeyError:
            raise ValueError(f"Codon {codon} is not valid.")

        if protein == "STOP":
            break

        protein_list.append(protein)

    return protein_list
