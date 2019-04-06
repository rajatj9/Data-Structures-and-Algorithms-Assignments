# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:48:29 2019

@author: jainr
"""

def f1(n):
    if n<=2:
        return 1
    else:
        return f1(n-1) + f1(n-2)
    

int_list = []
with open("input1.txt") as f:
    for x in f:
        int_list.append(int(x))

out_file = open('output1.txt', 'w')
    
for i in int_list:
    result = f1(i)
    print(result)
    out_file.write(str(result) + '\n')