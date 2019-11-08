#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:55:07 2019

@author: ai
"""

time = "0?:??"

def make_time(time):
    
    time = list(time)

    if time[4] == "?":
        time[4] = "9"

    if time[3] == "?":
        time[3] = "5"

    if time[1] == "?":
        if time[0] == "2" or "?":
            time[1] = "3"
        if time[0] == "1" or time[0] == "0":
            time[1] = "9"

    if time[0] == "?":
        if time[1] < "4":
            time[0] = "2"
        else:
            time[0] = "1"
        
    time_str = "".join(time)


    return time_str

make_time(time)
