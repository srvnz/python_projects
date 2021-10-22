#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:34:30 2021

@author: mr.hsp
"""


# %% C1: Add multiple variable arguments.
def multi_add(*arguments):
    result = 0
    for i in arguments:
        result += i
    return result

# %%% C1_result
print(multi_add(1, 2))
# This should give 3.
print(multi_add(1, 2, 3))
# This should give 6.
print(multi_add(4, 5, 10, 4))