#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guess a simple number

@author: mr.hsp
"""

import random

number = random.randint(1, 11)
guess = int(input('Guess a number between 1 and 10: '))

if guess == number:
    print(f'You are right! it was {number}')
elif guess - 2 <= number <= guess + 2:
    print(f'You were close! it was {number}')
else: 
    print(f'Nope! It was {number}')