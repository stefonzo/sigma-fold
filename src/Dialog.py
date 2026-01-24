#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 21:44:35 2025

@author: stephen
"""

import os
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

class Dialog(QDialog):
    """Abstraction for QDialog class."""
    def __init__(self, ui_filename, parent=None):
        super().__init__(parent)
        
        # loading the .ui file for our dialog box
        path = os.path.dirname(__file__)
        path = os.path.join(path, "..", "ui", ui_filename)
        uic.loadUi(path, self)