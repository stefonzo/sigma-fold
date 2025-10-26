#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 00:09:57 2025

@author: stefonzo
"""

import pyvista as pv
import numpy as np

class Visualizer():
    def __init__(self, widget):
        self.widget = widget
        self.width = 800
        self.height = 600
        
        # Scene data
        self.background_color = [0.2, 0.3, 0.4]  # RGB only for PyVista
        self.geometries = {}
        self.camera_settings = None
        
        # PyVista plotter (will be created lazily)
        self.plotter = None
        self.initialized = False
        
    def ensure_initialized(self):
        if not self.initialized:
            self.width = self.widget.width() if self.widget.width() > 0 else 800
            self.height = self.widget.height() if self.widget.height() > 0 else 600
            
            # Create offscreen plotter
            self.plotter = pv.Plotter(off_screen=True, window_size=[self.width, self.height])
            self.plotter.set_background(self.background_color)
            
            # Add geometries
            for name, geometry in self.geometries.items():
                self.plotter.add_mesh(geometry)
            
            self.initialized = True
    
    def on_resize(self, width, height):
        self.width = width
        self.height = height
    
    def render(self):
        self.ensure_initialized()
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