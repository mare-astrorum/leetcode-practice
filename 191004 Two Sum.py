# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:12:14 2019

@author: A
"""

nums = [3, 2, 4]
target = 6
answer = []

for i, num in enumerate(nums):
    print(i, num)
    for count in range(len(nums)-1):
        sum_i = nums[count] + nums[count+1]
        print(sum_i)
        if sum_i == target:
            first_ind = nums.index(nums[count])
            second_ind = nums.index(nums[count+1])
            answer.append(first_ind)
            answer.append(second_ind)
            print(answer)
            break





        answer = []
        index = 0
        for i, num in enumerate(nums):
#            print(index)
            if index < len(nums)-1:
                value = num + nums[index+1]
#                print(value)
                answer.append(value)
#                print(answer)
            index += 1
        
        
        answer2 = []
        for ind, c in enumerate(answer):
            if answer[ind] == target:
                first_ind = ind
                second_ind = ind+1
                answer2.append(first_ind)
                answer2.append(second_ind)
                return(answer2)

twoSum(nums, 9)


class Solution:
    def twoSum(self, nums, target):
        v_list = []
        answer = []
        for i, num in enumerate(nums):
            value = target - num
            print(value)
            v_list.append(value)
            print(v_list)
        
        for i, num in enumerate(nums):
            if num in v_list:
                answer.append(i)
                print(answer)
            
twoSum(self, nums, target)


for i, num in enumerate(nums):
    value = target - num
    if value in nums:
        if nums.index(value) != i:
            return [i, nums.index(value)]
    
for i,num in enumerate(nums):
    if (target-num) in nums:
        print(target-num)
        print(nums.index(target-num))
        if nums.index(target-num)!=i:
            return [i,nums.index(target-num)]