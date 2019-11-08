#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:33:24 2019

@author: ai
"""

num = 5


def countBits(num):

        import re
        arr = []
    
    
        for nr in range(num+1):
            print(nr)
            bit_num = bin(nr)
            print(bit_num)
            ones = re.findall("1", bit_num)
            print(ones)
            arr.append(len(ones))
            print(arr)
            print("---")
    
        return arr
    
countBits(num)
    
str(bin(5))


def countBits(num):
    dp = [0] * (num + 1)
    print(dp)
    exp = 0
    for i in range(1, num + 1):
        print(exp)
        print(i)
        if i == 2 ** exp:
            dp[i] = 1
            print(dp)
            exp += 1
        elif i < 2 ** exp:
            dp[i] = dp[2**(exp - 1)] + dp[i - 2**(exp - 1)]
            print(dp)
        print("---")
    
    return dp

