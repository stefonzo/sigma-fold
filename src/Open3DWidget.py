#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 20:21:11 2025

@author: stefonzo
"""

import numpy as np
from PyQt6.QtGui import QImage, QPainter
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
import Visualizer as vis

class Open3DWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget_visualizer = vis.Visualizer(self)
        
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.widget_visualizer.on_resize(self.width(), self.height())
        self.update() # make repaint happen (need to repaint after I've resized)
    
    def paintGL(self):
        # Get rendered image from visualizer
        o3d_image = self.widget_visualizer.render()
   
        # Convert to numpy
        np_array = np.asarray(o3d_image)
   
        # Get dimensions
        height, width, channels = np_array.shape
        bytesPerLine = channels * width
   
        # Create QImage
        qimage = QImage(np_array.data, width, height, bytesPerLine, QImage.Format_RGB888)
   
        # Paint it
        painter = QPainter(self)
        painter.drawImage(0, 0, qimage)
        painter.end()