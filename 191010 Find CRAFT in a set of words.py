#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:52:27 2019

@author: ai
"""

src = {"minecraftgame", "intelligent", "innercrafttalent", "knife", "scissor", "stonecrafter"}
key = "craft"

def find_words(src, key):
    end_list = []
    
    L = list(src)
    for word in L:
        if word.find(key) > 0:
            end_list.append(word)
            
    return set(end_list)