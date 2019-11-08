# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 12:23:43 2019

@author: A
"""

    
 
    
string = "abbcaezzd"


def unique_str(string):
    
    string_new = ""

    for a in string:
        count = string_new.count(a)
        if count < 1:
            string_new = string_new + a
    return len(string_new)
    