#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 01:21:22 2025

@author: stefonzo
"""

import App
import os
import sys
import numpy as np
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from Dialog import Dialog
from Molecule import Molecule
from Protein import Protein

class ControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Add src directory to path so uic can find custom widgets
        src_path = os.path.dirname(__file__)
        if src_path not in sys.path:
           sys.path.insert(0, src_path)
           
        # load ui file 
        path = os.path.dirname(__file__)
        path = os.path.join(path, "..", "ui", "control_window.ui")
        uic.loadUi(path, self)
        
        # menu actions (signals to slots)
        self.actionExport_as_PNG.triggered.connect(self.on_export_png)
        self.actionExit.triggered.connect(self.on_exit)
        self.actionMolfile.triggered.connect(self.on_open_molfile)
        self.actionFasta.triggered.connect(self.on_open_fasta)
        # molecule buttons
        self.visualizeSimMolecules.clicked.connect(self.on_visualize_molecules)
        # sim buttons
        self.startSimButton.clicked.connect(self.dummy)
        self.stepSimButton.clicked.connect(self.dummy)
        self.stopSimButton.clicked.connect(self.dummy)
        
    def on_open_molfile(self):
        filename, _ = QFileDialog.getOpenFileName(
                self,
                "Open Molecule File",
                "",
                "Mol Files (*.mol);;All Files (*)"
            )
        if filename:
            molecule = Molecule()
            molecule.load_mol(filename) # todo: add error handling for load_mol() method
            clean_filename = os.path.basename(filename)
            molecule.handle = clean_filename
            App.molecules = np.append(App.molecules, molecule)
            clean_filename = os.path.basename(filename)
            self.molecules_list.addItem(clean_filename)
        else:
            print("Invalid file name!")
        
            
    def on_open_fasta(self):
        fasta_protein = Protein()
        filename, _= QFileDialog().getOpenFileName(
                self,
                "Open fasta file",
                "",
                "Fasta Files (*.fasta);;All Files (*)"
            )
        App.proteins = np.append(App.proteins, fasta_protein.protein_from_fasta(filename))
        if filename:
            clean_filename = os.path.basename(filename)
            self.molecules_list.addItem(clean_filename)
        else:
            print("Invalid file name!")
        
    def on_save(self):
        return
    
    def on_save_as(self):
        return
    
    def on_about_program(self):
        return
    
    def on_export_png(self):
        export_dialog = Dialog("export_png_dialog.ui", self)
        pass
                
    def on_exit(self):
        self.close()
        
    def on_visualize_molecules(self): # todo: use molecule handles to select which molecule is visualized (handles can be obtained from QWidget)
        for molecule in App.molecules:
            self.pyVistaWidget.widget_visualizer.add_atoms_to_plotter(molecule)
        self.pyVistaWidget.widget_visualizer.plotter.reset_camera()
        self.pyVistaWidget.widget_visualizer.render()
        self.pyVistaWidget.update()
        
    def dummy(self):
        print("dummy")
        return
    
    