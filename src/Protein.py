from Molecule import Molecule
from Bio import SeqIO

class Protein(Molecule):
    def __init__(self):
        """Inherits from the Molecule class. Is used to simulate and visualize proteins in sigma-fold"""
        super().__init__() # calling parent (Molecule) constructor
        self.fasta_string = None
        
    def protein_from_fasta(self, filename):
        """Populates self.fasta_string with amino acid string sequence from a single fasta protein file"""
        fasta_file = SeqIO.read(filename, "fasta")
        self.fasta_string = fasta_file.format("fasta")
        