#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:06:57 2019

@author: ai
"""

s = ""
t = "ahbgdc"

letter = "x" 
def isSubsequence(s, t):

        if s == "":
            print("empty string")
        break
    
        index_list = []
    
        for letter in s:
            print(letter)
            if letter not in list(t):
                print("False")

            for ind, let in enumerate(t):
                print(ind, let)
                if letter == let:
                    index_list.append(ind)
                    print(index_list)
    
        
        for i in range(len(index_list)-1):
            if index_list[i] < index_list[i+1]
                return True
            else:
                return False    
            
