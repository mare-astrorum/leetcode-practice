# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:37:51 2019

@author: A
"""

B = [0, 9, 2, 15, 4, 91]
A = [7, 1, 11, 3, 15, 5]



def minSwap(A, B):
    n1, s1 = 0, 1
    for i in range(1, len(A)):
        i = 1
        n2 = s2 = float("inf")
        if A[i-1] < A[i] and B[i-1] < B[i]:
            n2 = min(n2, n1)
            s2 = min(s2, s1 + 1)
        if A[i-1] < B[i] and B[i-1] < A[i]:
            n2 = min(n2, s1)
            s2 = min(s2, n1 + 1)

        n1, s1 = n2, s2

    return min(n1, s1)


A = [1,3,5,4]
B = [1,2,3,7]


def solution(A, B):


    for i in range(0, len(A)-1):
        
        if A[i+1] > A[i] and B[i+1] < B[i]:
            print(A[i], A[i+1], B[i], B[i+1])
            swap+=1
#        elif A[i+1] < A[i] and B[i+1] > B[i]:
#            print(A[i], A[i+1], B[i], B[i+1])
#            swap+=1
    return swap
