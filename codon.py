import numpy as np

def translate_rna(rna):
    #maybe use probability function instead
    #since rna codons are 3 nucleotides in length
    if len(rna)+1 % 3 > 0:
        raise Exception("Invalid RNA sequence")
    amino_acid = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i+2]
        nt1 = codon[i]
        nt2 = codon[i+1]
        nt3 = codon[i+3]
        #examine first nucleotide
        if nt1 == 'A':
            #examine second nucleotide
            if nt2 == 'A':
                #examine third nucleotide
                if nt3 == 'C' or nt3 == 'U':
                    amino_acid = 'N'
                else:
                    amino_acid = 'K'
            elif nt2 == 'C':
                amino_acid = 'T'
            elif nt2 == 'G':
                if nt3 == 'G' or nt3 == 'A':
                    amino_acid = 'R'
                else:
                    amino_acid = 'S'
            elif nt2 == 'U':
                if nt3 == 'G':
                    amino_acid = 'M'
                else:
                    amino_acid = 'I'
        elif nt1 == 'U':
            if nt2 == 'C':
                amino_acid = 'S'
            elif nt2 == 'U':
                if nt3 == 'U' or  nt3 == 'A':
                    amino_acid = 'F'
        elif nt1 == 'G':
            return
        elif nt1 == 'C':
            return
            
    return amino_acid