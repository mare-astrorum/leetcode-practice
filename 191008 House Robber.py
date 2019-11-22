
"""
https://leetcode.com/problems/house-robber/
"""

# Version 1

nums = [1,2,3,1]



    def rob(nums):
    
    total = 0

    for ind, num in enumerate(nums):
        print(ind, num)
        if ind % 2 == 0:
            total += num
            print(total)

    return total


# Version 2, dynamic programming


nums = [1,2,3,1]

def rob(nums):

    length = len(nums)
			
    dp = [0]*length # assign dp array
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    print(dp[0], dp[1])
    print(dp)
    
    for i in range(2, length):
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        print(dp)
        print(dp[i-2]+nums[i], dp[i-1])
        print(dp[i])
        print("***")
    print(dp)
    print("-------")
    
    return max(dp)

rob(nums)


for i in range(1, 20):
    print(bin(i))