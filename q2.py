# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:12:28 2023

@author: benwy
"""

#QUESTION 2

from functools import reduce


A = [1, 2, 3]

B = [6, 5, 4]

print("A = [1, 2, 3]")

print("B = [6, 5, 4]")

def dot(A, B):
    if len(A) != len(B):
      return 0

    return sum(i[0] * i[1] for i in zip(A, B))

print("The dot product of A and B is " + str(dot(A, B)))

if len(A) != len(B):
    print("Size of vectors are not consistent")
    

def prod(val) : 
    res = 1 
    for ele in val: 
        res *= ele 
    return res  

C = [[1, 2],[3, 4]]

print("C = [[1, 2],[3, 4]]")

res = prod(list(reduce(lambda i, j: i & j, (set(x) for x in C))))

print ("The common row elements product is : " + str(res))