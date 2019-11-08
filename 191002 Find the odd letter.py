# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def extra_character(one_str, two_str):
    index = 0
    if len(one_str) > len(two_str):
        str2 = one_str
        str1 = two_str
    else:
        str1 = one_str
        str2 = two_str
        
    for letter in str1:
        if letter != str2[index]:
            extra_char = str2[index]
            return(extra_char)
        index+=1 

extra_character("google", "googgle")

ari = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
ari[2][2]