#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:22:34 2019

@author: ai
"""

A = [0, 3, 2]

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        peak_right = True
        peak_left = True
        
        
        if len(A) >= 3:
            peak = max(A)
            index = A.index(peak)
            
            if peak != A[0] and peak != A[-1]:    
                right_list = []
                for r in range(index, len(A)-1):
                    if A[r] > A[r+1]:
                        right = "T"
                        right_list.append("T")
                    else:
                        right_list.append("F")
                if "F" in right_list:
                    peak_right = False
                
                left_list = []        
                for r in range(0, index):
                    if A[r] < A[r+1]:
                        left = "T"
                        left_list.append("T")
                    else:
                        left_list.append("F")
                if "F" in left_list:
                    peak_left = False
                        
                if peak_right and peak_left:
                    return True
                    
                else:
                    return False