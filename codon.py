import numpy as np

def translate_rna(rna):
    #maybe use probability function instead
    #since rna codons are 3 nucleotides in length
    if len(rna)+1 % 3 > 0:
        raise Exception("Invalid RNA sequence")

    for i in range(0, len(rna), 3):
        codon = rna[i:i+2]
        