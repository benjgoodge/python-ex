# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:39:51 2023

@author: benwy
"""
#  QUESTION 3


import numpy as np

a = [5, 4, 9, 2, 0, 4, 7, -9]

anump = np.array([5, 4, 9, 2, 0, 4, 7, -9])

print(str(anump[-1]) + " is the last index in the array")

print(str(anump[1:6]) + " are the second to seventh indexes in the array")

print("When calling anump[:-2], we return all values of the array, except the penultimate and final 2 index:")

print(anump[:-2])

print("When calling anump[::2], we return every other value of the array, starting from the anump[0]:")

print(anump[::2])

print("Changing the last entry to -9 and returning anump[0:3] = 1 gives us the following:")

anump[0:3] = 1

print(anump[0:3])