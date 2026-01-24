#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 19:57:33 2025

@author: stephen

"""

import numpy as np

"""Dictionary used to store atomic information."""
atoms = {
    "H": {"symbol" : "H", "mass": 1.0080, "radius": 1.20, "pos": np.array([0.0, 0.0, 0.0]), "vel": np.array([0.0, 0.0, 0.0]), "acc": np.array([0.0, 0.0, 0.0]), "force" : np.array([0.0, 0.0, 0.0]), "charge" : 0},
    "C": {"symbol" : "C", "mass": 12.011, "radius": 1.70, "pos": np.array([0.0, 0.0, 0.0]), "vel": np.array([0.0, 0.0, 0.0]), "acc": np.array([0.0, 0.0, 0.0]), "force" : np.array([0.0, 0.0, 0.0]), "charge" : 0},
    "N": {"symbol" : "N", "mass": 14.007, "radius": 1.55, "pos": np.array([0.0, 0.0, 0.0]), "vel": np.array([0.0, 0.0, 0.0]), "acc": np.array([0.0, 0.0, 0.0]), "force" : np.array([0.0, 0.0, 0.0]), "charge" : 0},
    "O": {"symbol" : "O", "mass": 15.999, "radius": 1.52, "pos": np.array([0.0, 0.0, 0.0]), "vel": np.array([0.0, 0.0, 0.0]), "acc": np.array([0.0, 0.0, 0.0]), "force" : np.array([0.0, 0.0, 0.0]), "charge" : 0},
    "P": {"symbol" : "P", "mass": 30.97376200, "radius": 1.80, "pos": np.array([0.0, 0.0, 0.0]), "vel": np.array([0.0, 0.0, 0.0]), "acc": np.array([0.0, 0.0, 0.0]), "force" : np.array([0.0, 0.0, 0.0]), "charge" : 0},
    "S": {"symbol" : "S", "mass": 32.07, "radius": 1.80, "pos": np.array([0.0, 0.0, 0.0]), "vel": np.array([0.0, 0.0, 0.0]), "acc": np.array([0.0, 0.0, 0.0]), "force" : np.array([0.0, 0.0, 0.0]), "charge" : 0}
}