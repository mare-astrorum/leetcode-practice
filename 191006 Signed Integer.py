'''
https://leetcode.com/problems/reverse-integer/
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
            
        number_list = []
        negative_list = []
        
        str_x = str(x)
        for i in str_x:
            if i == "-":
                negative_list.append(i)
            else:
                number_list.append(i)
        
        number_list.reverse()
        
        number_string = "".join(number_list)
        number_string = number_string.lstrip("0")
            
        if negative_list:
            number_string = "-"+number_string
        
            
        if int(number_string) < -(2**31) or int(number_string) > (2**31)-1:
            return 0
        else:
            return number_string
        