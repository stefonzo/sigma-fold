# %%
#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 00:09:57 2025

@author: stefonzo
"""

import pyvista as pv
import App

radius_scale = 1.0

class Visualizer():
    def __init__(self, offscreen=True):
        self.width = 800 # see if I can make this more flexible (put this under settings)
        self.height = 600
        self.offscreen = offscreen
        
        # Scene data
        self.background_color = App.window_background_color  # RGB only for PyVista
        self.camera_settings = None
        
        # Create offscreen plotter immediately
        self.plotter = pv.Plotter(off_screen=self.offscreen, window_size=[self.width, self.height])
        self.plotter.set_background(self.background_color)
    
    def on_resize(self, width, height):
        self.width = width
        self.height = height
    
    def render(self):
         img = self.plotter.screenshot(return_img=True, transparent_background=False) # img is a np array
         return img  
    
    def export_to_png(self, width, height):
        return self.plotter.screenshot(return_img=True, transparent_background=False)
    
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
    