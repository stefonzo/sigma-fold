#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 00:09:57 2025

@author: stefonzo
"""

import pyvista as pv
import App

radius_scale = 0.75

class Visualizer():
    def __init__(self, offscreen=True):
        """pyvista visualizer for widget visualization, screenshotting, or offscreen rendering"""
        self.width = 800 # see if I can make this more flexible (put this under settings)
        self.height = 600
        self.offscreen = offscreen
        self.background_color = App.window_background_color  
        self.camera_settings = None
        
        self.plotter = pv.Plotter(off_screen=self.offscreen, window_size=[self.width, self.height])
        self.plotter.set_background(self.background_color)
    
    def on_resize(self, width, height):
        """Called by PyVistaWidget.resizeEvent"""
        self.width = width
        self.height = height
    
    def render(self):
        """Called by PyVistaWidget.paintEvent"""
        img = self.plotter.screenshot(return_img=True, transparent_background=False) # img is a np array
        return img  
    
    def export_to_png(self, width, height):
        return self.plotter.screenshot(return_img=True, transparent_background=False)
    
    def get_sphere_mesh_from_atom(self, atom):
        """Returns pyvista.PolyData using atomic information from atoms dictionary in Atoms.py"""
        atomic_radius = atom["radius"] * radius_scale
        atomic_coords = atom["pos"]
        mesh = pv.Sphere(radius=atomic_radius, center=atomic_coords, theta_resolution=60, phi_resolution=60)   
        return mesh 
    
    def get_color_from_atom(self, atom):
        """Returns list of uniform floats [0.0, 1.0] to represent RGB color for atom using atomic symbol from atoms dictionary in Atoms.py"""
        if atom["symbol"] == "H":
            return [1.0, 1.0, 1.0]
        elif atom["symbol"] == "C":
            return [0.0, 0.0, 0.0]
        elif atom["symbol"] == "O":
            return [1.0, 0.0, 0.0]
        elif atom["symbol"] == "P":
            return [0.0, 0.0, 1.0]
        elif atom["symbol"] == "N":
            return [0.0, 1.0, 0.0]
        else:
            print(f"color not defined for atom with symbol: {atom["symbol"]}")
            return [0.5,0.5,0.5]
    
    def add_atoms_to_plotter(self, molecule):
        """Goes through a molecule and stores atom and color info from molecule into plotter for future rendering"""
        for atom in molecule.atoms:
            self.plotter.add_mesh(mesh=self.get_sphere_mesh_from_atom(atom), color=self.get_color_from_atom(atom))