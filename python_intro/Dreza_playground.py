#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:35:34 2021

@author: mr.hsp
"""


# %% C1
def func1(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


def func2(num, x=1):
    return num ** x


def multi_add(*args):
    result = 0
    for i in args:
        result = result + i
    return result


# %% C2
print(func1(3, 4))
print(func2(3, 4))
print(multi_add(1, 2, 3))
