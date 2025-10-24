#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 01:21:22 2025

@author: stefonzo
"""

import os
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

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
    
    def on_open(self):
        return
    
    def on_save(self):
        return
    
    def on_save_as(self):
        return
    
    def on_exit(self):
        return
    
    