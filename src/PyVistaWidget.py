#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 20:21:11 2025

@author: stefonzo
"""

import numpy as np
from PyQt6.QtGui import QImage, QPainter
from PyQt6.QtWidgets import QWidget
import Visualizer as vis

class PyVistaWidget(QWidget):  
    def __init__(self, parent=None):
        """Used to display pyvista visualizer to qt ControlWindow"""
        super().__init__(parent)
        self.widget_visualizer = vis.Visualizer()
        
    def resizeEvent(self, event):
        """Called when widget in ControlWindow is resized"""
        super().resizeEvent(event)
        self.widget_visualizer.on_resize(self.width(), self.height())
        self.update()
    
    def paintEvent(self, event):
        """Updates widget display"""
        np_array = self.widget_visualizer.render()
        
        # Ensure array is contiguous in memory (required for QImage)
        if not np_array.flags['C_CONTIGUOUS']:
            np_array = np.ascontiguousarray(np_array)
        
        # Get dimensions
        height, width, channels = np_array.shape
        bytesPerLine = channels * width
        
        # Create QImage - need to convert to bytes (this is needed for custom Qt widget!)
        qimage = QImage(np_array.tobytes(), width, height, bytesPerLine, QImage.Format.Format_RGB888)
        scaled_qimage = qimage.scaled(self.width(), self.height())
        
        # Paint it
        painter = QPainter(self)
        painter.drawImage(0, 0, scaled_qimage)
        painter.end()