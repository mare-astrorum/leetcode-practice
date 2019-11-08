HOUSE ROBBER

Example 1:

nums = [1,2,3,1]
Output: 4

Example 2:

nums = [2,7,9,3,1]
Output: 12

def rob(nums):

    length = len(nums)
    if length==0:
        return 0
    if length==1:
        return nums[0]
    if length==2:
        return max(nums)
	
'''Create an array for answers'''		
    dp = [0]*length # assign dp array
'''Pick the largest response'''
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    
    '''Move through the array and pick the answer'''
    for i in range(2, length):
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])

    return max(dp)


