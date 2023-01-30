# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:44:26 2023

@author: benwy
"""

# QUESTION 4

# generate random integer values (r)
import numpy as np
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt
# seed random number generator
seed(1)
# generate some integers
r = randint(1, 9, 20)
print(r)




# Original array

r1 = np.mean(r)
print("\nMean: ", r1)

r2 = np.std(r)
print("\nstd: ", r2)

r3 = np.var(r)
print("\nvariance: ", r3)



count, bins, ignored = plt.hist(r, 20, density=True)
plt.plot(bins, 1/(r2 * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - r1)**2 / (2 * r2**2) ),
         linewidth=2, color='r')
plt.show()