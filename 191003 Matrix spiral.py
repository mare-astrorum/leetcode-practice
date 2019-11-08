# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:36:07 2019

@author: A
"""

inty = 3
number = 3**2

values = list(range(1, number))

Matrix = [[0 for x in range(inty)] for y in range(inty)] 

middle = round(3/2) - 1

Matrix[middle][middle] = number

Matrix[middle][middle-1] = number-1


index = 0
for i in Matrix[middle+1]:
    start = number-1
    print(start)
    Matrix[middle+1][index] = start-1
    print(Matrix[middle+1][index])
    index+=1
    print(index)
    number-=1

Matrix[middle][middle+1] = start-2

index = 0
start = 0
for i in Matrix[middle-1]:
    number = start+1
    Matrix[middle-1][index] = number
    index+=1
    number+=1
    