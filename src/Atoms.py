#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 19:57:33 2025

@author: stephen

"""

import numpy as np

atoms = {
    "H": {"mass": 1.0080, "radius": 120, "pos": np.array([0.0, 0.0, 0.0]), "vel": np.array([0.0, 0.0, 0.0]), "acc": np.array([0.0, 0.0, 0.0]), "force" : np.array([0.0, 0.0, 0.0]), "charge" : 0},
    "C": {"mass": 12.011, "radius": 170, "pos": np.array([0.0, 0.0, 0.0]), "vel": np.array([0.0, 0.0, 0.0]), "acc": np.array([0.0, 0.0, 0.0]), "force" : np.array([0.0, 0.0, 0.0]), "charge" : 0},
    "N": {"mass": 14.007, "radius": 155, "pos": np.array([0.0, 0.0, 0.0]), "vel": np.array([0.0, 0.0, 0.0]), "acc": np.array([0.0, 0.0, 0.0]), "force" : np.array([0.0, 0.0, 0.0]), "charge" : 0},
    "O": {"mass": 15.999, "radius": 152, "pos": np.array([0.0, 0.0, 0.0]), "vel": np.array([0.0, 0.0, 0.0]), "acc": np.array([0.0, 0.0, 0.0]), "force" : np.array([0.0, 0.0, 0.0]), "charge" : 0},
    "P": {"mass": 30.97376200, "radius": 180, "pos": np.array([0.0, 0.0, 0.0]), "vel": np.array([0.0, 0.0, 0.0]), "acc": np.array([0.0, 0.0, 0.0]), "force" : np.array([0.0, 0.0, 0.0]), "charge" : 0},
    "S": {"mass": 32.07, "radius": 180, "pos": np.array([0.0, 0.0, 0.0]), "vel": np.array([0.0, 0.0, 0.0]), "acc": np.array([0.0, 0.0, 0.0]), "force" : np.array([0.0, 0.0, 0.0]), "charge" : 0}
}