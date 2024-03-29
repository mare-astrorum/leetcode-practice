"""
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
"""


# MINIMUM DOMINO ROTATIONS

A = [2,1,2,2] #k:2, v:3
B = [5,2,3,6] #k:2, v:1

import collections

class Solution:
    
    def minDominoRotations(A, B):
        
        # If the input is None 
        if not A or not B: 
            return -1
        if len(list(set(A))) == 1 or len(list(set(B))) == 1:
            return 0
        
        # Create a dictionary of keys and values
        A_count = collections.Counter(A)
        B_count = collections.Counter(B)

        # Find max values
        for key, value in A_count.items():
            if value == max(A_count.values()):
                 A_max_freq = key

        for key, value in B_count.items():
            if value == max(B_count.values()):
                 B_max_freq = key 
      
        A_swaps = 0
        B_swaps = 0

        # One of them has to be maximum frequency
        for i in range(len(A)):
            if A[i] != A_max_freq:
                if B[i] != B_max_freq:
                    return -1
                A_swaps += 1 # If it is max freq, add how many
            if B[i] != B_max_freq:
                if A[i] != B_max_freq: 
                    return -1
                B_swaps += 1
        
        if A_swaps > B_swaps:
            return B_swaps
        else:
            return A_swaps
                
                
                
        

