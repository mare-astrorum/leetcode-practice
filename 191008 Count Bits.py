"""
https://leetcode.com/problems/counting-bits/
"""

num = 5

# Version 1

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


# Version 2

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

