#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:44:28 2019

@author: ai
"""

import re

nums = [0,1,2,2,3,0,4,2]
val = 2


for i in range(len(nums)):
    if val in nums:
        nums.remove(val)

print(len(nums))