#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 17:22:14 2021
@author: mr.hsp
"""


# %% C1: if_else for temperature
temp = int(input('What temperature is your water? '))

if temp <= 0:
    print("It's freezing!")
elif temp >= 100:
    print("It's boiling!")
else:
    print("The temperature is safe.")

# %%% C1_result:


# %% C2: Compare two numbers
def compare(x, y):
    if (x < y):
        statement = 'x is less than y'
    elif (x > y):
        statement = 'x is greater than y'
    else:
        statement = 'x equals y'
    return print(statement)


# %%% C2_result:
compare(0, 1)

# %% C3: Conditional statement with only two conditions
x, y = 1000, 100
statement = 'x is less than y' if (x < y) else 'x is the same'
print(statement)
