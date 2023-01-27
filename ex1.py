# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:44:18 2023

@author: benwy
"""
import math
import numpy as np

from math import pi


# Calculation of PI using Leibniz formula

# Function to calcultae PI using Leibniz
def leibniz(n):
    t_sum = 0
    for i in range(n):
        term = (-1) ** i /(2*i+1)
        t_sum = t_sum + term
    
    return t_sum * 4

# Reading number of terms to be considered in Leibniz formula
terms = int(input("Enter number of terms: "))

# Function call
pi1 = leibniz(terms)

# Displaying result
print("Pi = ", pi1)


#Calculating Mean Absolute Error

print("ABS error = ",abs(pi-pi1))

if abs(pi-pi1) < 1e-07:
    print("ABS error is less than 10^-7")
    
if abs(pi-pi1) > 1e-07:
    print("ABS error is more1 than 10^-7")

# N is between 10 000 000 and 100 000 000

