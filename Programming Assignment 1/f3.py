# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:56:24 2019

@author: jainr
"""

import numpy as np

G = np.array([[0,1],[1,1]])
def Power_of_G(n):
    if n==1:
        return G;
    else:
        if n%2 == 0:
            H = Power_of_G(n/2);
            return np.dot(H,H)
        else:
            H = Power_of_G((n-1)/2)
            return np.dot(H, np.dot(H,G))
        
def f3(n):
    temp = Power_of_G(n)
    return temp[0][1]

int_list = []
with open("input3.txt") as f:
    for x in f:
        int_list.append(int(x))

out_file = open('output3.txt', 'w')
    
for i in int_list:
    result = f3(i)
    print(result)
    out_file.write(str(result) + '\n')