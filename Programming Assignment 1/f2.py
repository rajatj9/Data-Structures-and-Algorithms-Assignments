# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:47:51 2019

@author: jainr
"""

def f2(n):
    if n<=2:
        return 1
    else:
        p=1
        q=1
        for i in range(3,n+1):
            r = p+q
            p = q
            q = r
        return r
    
    
int_list = []
with open("input2.txt") as f:
    for x in f:
        int_list.append(int(x))

out_file = open('output2.txt', 'w')
    
for i in int_list:
    result = f2(i)
    print(result)
    out_file.write(str(result) + '\n')