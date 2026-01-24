#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 19:55:41 2026

@author: stephen
"""
# for now this is a singleton class

from Visualizer import Visualizer

class InteractiveVisualizer(Visualizer):
    def __init__(self, molecules): 
        """Inherits from the Visualizer class and is used for interactive pyvista visualization"""
        super().__init__(offscreen=False)
        self.init_PyVista_window(molecules)
    
    def init_PyVista_window(self, molecules): 
        """Gets pyvista.Polydata representing atoms in molecule for InteractiveVisualizer"""
        for molecule in molecules:
            self.add_atoms_to_plotter(molecule)
    
    def open_PyVista_window(self): 
        """Called by ControlWindow.on_open_PyVista_window"""
        self.plotter.show(window_size = [self.width, self.height], title="Interactive Visualizer", interactive=True) # display the plotting window (https://docs.pyvista.org/api/plotting/_autosummary/pyvista.plotter)
    
    def close_PyVista_window(self): # this method might not be necessary  and could be deleted in the future if I don't end up doing anything with it
        pass