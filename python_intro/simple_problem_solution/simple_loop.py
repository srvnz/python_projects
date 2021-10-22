#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:28:23 2021

@author: mr.hsp
"""


# %% C1: Simple while loop
def main(x):
    while (x < 5):
        # x += 1
        print(x)
        x += 1


# %%% C1_result
main(0)

# %% C2: Simple for loop
for x in range(0, 5):
    print(x)

# %% C3: For loop over things
# For loops operate over sets of things not just numbers.
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for i in days:
    print(i)

# %% C4: For loop with breaks
for x in range(5, 10):
    if (x == 7):
        break
    print(x)

# %% C5: For loop with continue
for x in range(5, 10):
    # even numbers will be skipped from the loop.
    if (x % 2 == 0):
        continue
    print(x)

# %% C6: Loop with indexing
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for i, d in enumerate(days):
    print(i, d)