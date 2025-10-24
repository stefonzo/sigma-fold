#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 00:09:57 2025

@author: stefonzo
"""

import open3d as o3d

class Visualizer():
    def __init__(self, widget):
        self.widget = widget
        self.width = self.widget.width() if self.widget.width() > 0 else 800
        self.height = self.widget.height() if self.widget.height() > 0 else 600
        
        # KEY CHANGE: Don't create the renderer yet - just store None
        self.open3dVisualizer = None
        self.initialized = False
        
    def ensure_initialized(self):
        """
        Lazy initialization - only create the renderer when we first need it.
        By this time, the OpenGL context will be ready.
        """
        if not self.initialized:
            self.open3dVisualizer = o3d.visualization.rendering.OffscreenRenderer(
                self.width, self.height
            )
            self.init_visualizer()
            self.initialized = True
        
    def on_resize(self, width, height):
        self.width = width
        self.height = height
        # Recreate the renderer with new dimensions
        self.open3dVisualizer = o3d.visualization.rendering.OffscreenRenderer(
            width, height
        )
        self.init_visualizer()
        self.initialized = True
        
    def init_visualizer(self):
        # Set the background color (blue-ish gray)
        self.open3dVisualizer.scene.set_background([0.2, 0.3, 0.4, 1.0])
    
    def render(self):
        # KEY CHANGE: Make sure we're initialized before rendering
        self.ensure_initialized()
        return self.open3dVisualizer.render_to_image()
    
    def start_visualizer(self):
        return