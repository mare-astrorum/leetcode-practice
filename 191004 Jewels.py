
"""
https://leetcode.com/problems/jewels-and-stones/
"""

import re

J = "aA"
S = "aAAbbbb"

class Solution:
    def numJewelsInStones(self, J, S):
        answer = []
        for j in J:
            stones = re.findall(j, S)
            answer = answer + stones
        return len(answer)