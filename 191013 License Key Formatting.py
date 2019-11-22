'''
https://leetcode.com/problems/license-key-formatting/
'''

#LICENSE KEY FORMATTING

s = S[::-1].replace("-", "").upper()
i, j = 0, K
result = []

while j < len(s):
    result.insert(0, s[i:j][::-1])
    i = j
    j += K
result.insert(0, s[i:j][::-1])
return "-".join(result)

