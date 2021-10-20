#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculate the area and circumference of a circle.

@author: mr.hsp
"""
# %% C1: Packages
from math import pi

# %% C2: Function for area
def area(r):
    return pi * r ** 2

# %% C3: Function for circumference
def circumference(r):
    return pi * 2 * r

# %% C4: Input
radius = float(input('Circle radius: '))

# %% C5: Output
print(f'Area: {area(radius)}')
print(f'Circumference: {circumference(radius)}')
