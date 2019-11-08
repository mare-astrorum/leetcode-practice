# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:26:31 2019

@author: A
"""
import re

J = "aA"
S = "aAAbbbb"

#answer = 0
#for j in J:
#    if j in S:
#        answer += 1
#print(answer)

cutoff = 1
S = S[:cutoff] + S[cutoff+1:]

answer = []

for j in J:
    stones = re.findall(j, S)
    answer = answer + stones
print(len(answer))
    
    
[1, 2] + [2, 3]
