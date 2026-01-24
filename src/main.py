#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 01:22:03 2025

@author: stefonzo
"""

from PyQt6.QtWidgets import QApplication
import ControlWindow as cw

def main():
    """Runs the QApplication and Qt control window"""
    app = QApplication([])
    control_window = cw.ControlWindow()
    control_window.show()
    app.exec()

main()