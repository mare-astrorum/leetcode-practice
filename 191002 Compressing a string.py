# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 19:14:56 2019

@author: A
"""

import re


# 3[abc]4[ab]c

result = 3 * "abc" + 4 * "ab" + "c"




seq = "3[abc]4[ab]c"
seq2 = seq.replace("[", "*")
seq3 = seq2.replace("]", "+")


index = 1
for i in seq4:
    try:
        x = int(i)
        if x in range(10000):
            print(x)
        else: 
            continue
        if seq4[index] not in range(10000):
            print(int(i) * seq4[index])

       
seq = "3[abc]4[ab]c"
seq2 = seq.replace("[", " ")
seq3 = seq2.replace("]", " ")
seq4 = seq3.split()

result = []  
numbers = re.findall("[0-9]", seq)

index = 0
for i in seq4:
    print(i)
    if i in numbers:
        print(i)
        print(numbers)
        new_seq = int(i) * seq4[1]
        print(new_seq)
        result.append(new_seq)
        seq4 = seq4[1:]
        print(seq4)
        numbers.remove(i)
        print(numbers)
        index+=1
        print(index)
    else:
#        if seq4[index+1] not in numbers:
#            seq4.insert(1, 1)
        seq4 = seq4[1:]
        index+=1


del seq4[0:2]
seq4.insert(0, new_seq)
    
    
for i in numbers:
    if i in seq4:
        new_seq = int(i) * seq4[index+1]
        print(new_seq)
        print(i)

re.findall("[0-9]", seq)
re.search("[0-9]", seq)
re.finditer("[0-9]", seq)
re.match("3", seq)
re.split("[\[\]]", seq)
