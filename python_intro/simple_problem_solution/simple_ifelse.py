#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 17:22:14 2021

@author: mr.hsp
"""

temp = int(input('What temperature is your water? '))

if temp <= 0:
    print("It's freezing!")
elif temp >= 100:
    print("It's boiling!")
else:
    print("The temperature is safe.")