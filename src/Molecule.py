#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 19:57:42 2025

@author: stephen
"""

from Atoms import atoms
from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np

class Molecule():
    """Wrapper for rdkit Mol object and contains custom representations of data for simulation."""
    def __init__(self):
        self.rdkit_mol = None
        self.atoms = np.array([])
        self.bonds = np.array([])
        
    def atoms_from_rdkitmol(self):
        return np.array([])
    
    def bonds_from_rdkitmol(self):
        return np.array([])
        
    def load_mol(self, path):
        self.rdkit_mol = Chem.MolFromMolFile(path)
        if self.rdkit_mol is None:
            raise ValueError(f"Could not parse molecule from file: {path}")
        self.atoms = self.atoms_from_rdkitmol()
        self.bonds = self.bonds_from_rdkitmol()
        
    def __str__(self):
        pass