# %%
#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 00:09:57 2025

@author: stefonzo
"""

import pyvista as pv
import numpy as np

radius_scale = 0.005

class Visualizer():
    def __init__(self, widget):
        self.widget = widget
        self.width = 800 # see if I can make this more flexible
        self.height = 600
        
        # Scene data
        self.background_color = [0.2, 0.3, 0.4]  # RGB only for PyVista
        self.geometries = np.array([])
        self.camera_settings = None
        
        # Create offscreen plotter immediately
        self.plotter = pv.Plotter(off_screen=True, window_size=[self.width, self.height])
        self.plotter.set_background(self.background_color)
    
    def on_resize(self, width, height):
        self.width = width
        self.height = height
    
    def render(self):
        # Render and return as numpy array
         img = self.plotter.screenshot(return_img=True, transparent_background=False)
         return img  # Returns numpy array directly!
    
    def export_to_png(self, width, height):
        # Create temporary plotter at export resolution
        export_plotter = pv.Plotter(off_screen=True, window_size=[width, height])
        export_plotter.set_background(self.background_color)
        
        # Add geometries
        for name, geometry in self.geometries.items():
            export_plotter.add_mesh(geometry)
        
        # Render to image
        img = export_plotter.screenshot(return_img=True, transparent_background=False)
        export_plotter.close()  # Clean close - no segfaults!
        return img
    
    def get_sphere_mesh_from_atom(self, atom):
        atomic_radius = atom["radius"] * radius_scale
        atomic_coords = atom["pos"]
        mesh = pv.Sphere(radius=atomic_radius, center=atomic_coords)   
        return mesh 
    
    def get_color_from_atom(self, atom):
        if atom["symbol"] == "H":
            return [1.0, 1.0, 1.0]
        elif atom["symbol"] == "C":
            return [0.0, 0.0, 0.0]
        elif atom["symbol"] == "O":
            pass
        elif atom["symbol"] == "P":
            pass
        elif atom["symbol"] == "N":
            pass
        else:
            print(f"color not defined for atom with symbol: {atom["symbol"]}")
            return [0.5,0.5,0.5]
    
    def add_atoms_to_plotter(self, molecule):
        for atom in molecule.atoms:
            self.plotter.add_mesh(mesh=self.get_sphere_mesh_from_atom(atom), color=self.get_color_from_atom(atom))
            #self.geometries = np.append(geometries, )
    