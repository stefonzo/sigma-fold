from Molecule import Molecule
from Bio import SeqIO

class Protein(Molecule):
    def __init__(self):
        super().__init__() # calling parent (Molecule) constructor
        self.fasta_string = None
        
    def protein_from_fasta(self, filename):
        fasta_file = SeqIO.read(filename, "fasta")
        self.fasta_string = fasta_file.format("fasta")
        