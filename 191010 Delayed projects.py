#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 12:27:19 2019

@author: ai
"""

K = len(L) = no of dependencies
L = []

J = len(D) = no of delayed projects
D = []

C = no of test cases


[0] 3 test cases [1]
[1] 2 dep 1 delay
[2] B dep on A
[3] C dep on B
[4] B is delayed

[5]5 dep 2 del [2]
P
P
Q
R
S
Q S ""

with open('filename') as f:
    C = f.readlines()



C = ["3", "2 1", "B A", "C B", "B", "5 2", ["P Q"], ["P S"], ["Q R"]]

C = ["3", "2 1", "B A", "C B", "B", "5 2"]
C[0]



with open("file.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)


def list_output(line):

    if C < 1 or C > 20:
    return -1
    if K < 1 or K > 100:
    return -1
    if J < 1 or J > 26:
    return -1


    initial_delayed_list = []
    final_delayed_list = []

i = 1

    for i in range(0, len(C[0])+1):
        no_test_cases = int(C[i]) #3
        location_delayed = no_test_cases+1
        initial_delayed_list.append(C[location_delayed])
        

        for i in range(i+1, no_test_cases+1):
            line = C[i]
            print(line)
            for value in initial_delayed_list:
                if proj[2] == value:
                    final_delayed_list.append(proj[0])
        
    
    end_list = initial_delayed_list + final_delayed_list
    end_list_unique = list(set(end_list)))

    return 'Case #' + str(C[i]) + ': "".join(end_list_unique)'
        
    



    
