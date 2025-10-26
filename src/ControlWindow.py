#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 01:21:22 2025

@author: stefonzo
"""

import os
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from Dialog import Dialog

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
        print(path)
        uic.loadUi(path, self)
        
        # connecting menu actions (signals to slots)
        self.actionExport_as_PNG.triggered.connect(self.on_export_png)
        self.actionExit.triggered.connect(self.on_exit)
    
    def on_open(self):
        return
    
    def on_save(self):
        return
    
    def on_save_as(self):
        return
    
    def on_about_program(self):
        return
    
    def on_export_png(self):
        export_dialog = Dialog("export_png_dialog.ui", self)
        
        if export_dialog.exec() == Dialog.DialogCode.Accepted:
            width = export_dialog.widthSpinBox.value()
            height = export_dialog.heightSpinBox.value()
            
            filename, _ = QFileDialog.getSaveFileName(self, "Export PNG", "", "PNG Files (*.png)")
            
            if filename:
                if not filename.endswith(".png"):
                    filename += ".png"
                
                # Get numpy array directly from PyVista
                np_array = self.pyVistaWidget.widget_visualizer.export_to_png(width, height)
                
                # Save with PIL
                from PIL import Image
                pil_image = Image.fromarray(np_array)
                pil_image.save(filename)
                
                print(f"Exported {width}x{height} PNG to: {filename}")
                
    def on_exit(self):
        self.close()
    
    