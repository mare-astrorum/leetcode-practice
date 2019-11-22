"""
https://leetcode.com/problems/valid-palindrome-ii/
"""

s = "aba"
s_reverse = s[::-1]

if s == s_reverse:
    print("true")
    

s = "cbbcc"
s_reverse = s[::-1]

for ind, letter in enumerate(s):
    print(ind, letter, s_reverse[ind])
    
    if letter != s_reverse[ind]:
        print(letter)
        s_list = list(s)
        print(s_list)
        s_list.pop(ind)
        print(s_list)
        s = "".join(s_list)
        print(s)
        s_reverse = s[::-1]
        print(s_reverse)
        if s == s_reverse:
            print("true")
            break
        else:
            print("false")
            break



ind = 3   
s = s[:ind]+s[ind+1:]  
    