#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 19:57:42 2025

@author: stephen
"""

from Atoms import atoms
from rdkit import Chem
from rdkit.Chem import AllChem # need this to use Chem.rdMolDescriptors.CalcMolFormula
import numpy as np

class Molecule():
    def __init__(self):
        """Wrapper for rdkit Mol object and contains custom representations of data for simulation"""
        self.rdkit_mol = None
        self.atoms = np.array([])
        self.bonds = np.array([])
        self.molecular_formula = None
        self.num_atoms = None
        self.name = None
        self.description = None
        self.handle = None # used in ControlWindow.py (Qt stuff)
        
    def atoms_from_rdkitmol(self): 
        """Gets conformer from self.rdkit_mol and uses conformer's atomic symbols and atomic coordinates to populate atoms in self.atoms"""
        AllChem.EmbedMolecule(self.rdkit_mol)
        AllChem.UFFOptimizeMolecule(self.rdkit_mol)
        self.rdkit_mol.GetConformer()
        
        for i, atom in enumerate(self.rdkit_mol.GetAtoms()): # (https://stackoverflow.com/questions/71915443/rdkit-coordinates-for-atoms-in-a-molecule)
            symbol = atom.GetSymbol()
            sim_atom = None
            if symbol in atoms:
                sim_atom = atoms[symbol].copy() # need to use copy with a dictionary entry otherwise I'll just be using the same reference across atoms...?
            else:
                print(f"Atom not recognized: {symbol}")
                continue
            rdkit_pos = self.rdkit_mol.GetConformer().GetAtomPosition(i)
            dict_pos = np.array([rdkit_pos.x, rdkit_pos.y, rdkit_pos.z]) # convert positions to a numpy  array
            sim_atom["pos"] = dict_pos # use position data for value in dict
            self.atoms = np.append(self.atoms, sim_atom)
    
    def bonds_from_rdkitmol(self): 
        """Populates self.bonds with bond information from self.rdkit_mol"""
        return np.array([])
        
    def load_mol(self, path):
        """Populates self.rdkit_mol from a single molfile"""
        self.rdkit_mol = Chem.MolFromMolFile(path)
        if self.rdkit_mol is None: # todo: better error handling
            raise ValueError(f"Could not parse molecule from file: {path}")
        self.rdkit_mol = Chem.AddHs(self.rdkit_mol) # add hydrogen atoms to loaded molecule
        self.atoms_from_rdkitmol()
        self.bonds = self.bonds_from_rdkitmol()
        self.molecular_formula = Chem.rdMolDescriptors.CalcMolFormula(self.rdkit_mol)
        self.num_atoms = self.rdkit_mol.GetNumAtoms(onlyExplicit=False) # using this argument so light atoms are included in the count
        
    def __str__(self):
        return f"Molecular Formula: {self.molecular_formula}\nNumber of atoms: {self.num_atoms}\nName: {self.name}\nDescription: {self.description}"