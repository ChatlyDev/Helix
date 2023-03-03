from Bio.Graphics import *
from Bio.Seq import Seq
from Bio.PDB.MMCIFParser import MMCIFParser
from Bio.PDB.Polypeptide import Polypeptide
from Bio.PDB.StructureBuilder import StructureBuilder

parser = MMCIFParser()

    
    
#create a function that shows 3d models of proteins
def show_3d(pdb_code):
    #get the structure of the protein
    structure = parser.get_structure(pdb_code)
    #show it
    ppb = PPBuilder()
    show_structure(structure)

#create a function that shows the sequence of a protein
def show_sequence(pdb_code):
    #get the structure of the protein
    structure = parser.get_structure(pdb_code)
    #get the residues
    ppb = PPBuilder()
    for pp in ppb.build_peptides(structure):
        #show the sequence
        print(pp.get_sequence())

#create a function that shows the secondary structure of a protein
def show_secondary_structure(pdb_code):
    #get the structure of the protein
    structure = parser.get_structure(pdb_code)
    #get the secondary structure
    ppb = PPBuilder()
    for pp in ppb.build_peptides(structure):
        #show the secondary structure
        print(pp.get_sec_struct())

#create a function that shows the sequence and secondary structure of a protein
def show_sequence_and_secondary_structure(pdb_code):
    #get the structure of the protein
    structure = parser.get_structure(pdb_code)
    #get the residues
    ppb = PPBuilder()
    for pp in ppb.build_peptides(structure):
        #show the sequence
        print(pp.get_sequence())
        #show the secondary structure
        print(pp.get_sec_struct())

#create a function that shows the sequence and secondary structure of a protein
def show_sequence_and_secondary_structure_with_gaps(pdb_code):
    #get the structure of the protein
    structure = parser.get_structure(pdb_code)
    #get the residues
    ppb = PPBuilder()
    for pp in ppb.build_peptides(structure):
        #show the sequence
        print(pp.get_sequence())
        #show the secondary structure
        print(pp.get_sec_struct_with_gaps())

#create a function that shows the sequence and secondary structure of a protein
def show_sequence_and_secondary_structure_with_gaps_and_missing_residues(pdb_code):
    #get the structure of the protein
    structure = parser.get_structure(pdb_code)
    #get the residues
    ppb = PPBuilder()
    for pp in ppb.build_peptides(structure):
        #show the sequence
        print(pp.get_sequence())
        #show the secondary structure
        print(pp.get_sec_struct_with_gaps_and_missing_residues())

#create a function that shows the sequence and secondary structure of a protein
def show_sequence_and_secondary_structure_with_gaps_and_missing_residues_and_disordered_residues(pdb_code):
    #get the structure of the protein
    structure = parser.get_structure(pdb_code)
    #get the residues
    ppb = PPBuilder()
    for pp in ppb.build_peptides(structure):
        #show the sequence
        print(pp.get_sequence())
        #show the secondary structure
        print(pp.get_sec_struct_with_gaps_and_missing_residues_and_disordered_residues())

#create a function that shows the sequence and secondary structure of a protein
def show_sequence_and_secondary_structure_with_gaps_and_missing_residues_and_disordered_residues_and_insertions(pdb_code):
    #get the structure of the protein
    structure = get_structure(pdb_code)
    #get the residues
    ppb = PPBuilder()
    for pp in ppb.build_peptides(structure):
        #show the sequence
        print(pp.get_sequence())
        #show the secondary structure
        print(pp.get_sec_struct_with_gaps_and_missing_residues_and_disordered_residues_and_insertions())

#create a function that shows the sequence and secondary structure of a protein
def show_sequence_and_secondary_structure_with_gaps_and_missing_residues_and_disordered_residues_and_insertions_and_terminal_residues(pdb_code):
    #get the structur of the protein
    structure = get_structure(pdb_code)
    #get the residues
    ppb = PPBuilder()
    for pp in ppb.build_peptides(structure):
        #show the sequence
        print(pp.get_sequence())
        #show the secondary structure
        print(pp.get_sec_struct_with_gaps_and_missing_residues_and_disordered_residues_and_insertions_and_terminal_residues())