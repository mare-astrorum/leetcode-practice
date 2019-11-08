# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:24:58 2019

@author: A
"""

((apple, 120), (banana, 200), (apple, 150))

apple min 120, mean 135, max 150
banana 200, 200, 200


C = 5

5

apple 120

banana 200

apple 150

string = "5\n\napple 120\n\nbanana 200\n\napple 150"



#L = ["5", "", "apple 120", "", "banana 200", "", "apple 150]

def convert_string(string):

    L = string.split("\n")
    clean_L = []
    for s in L:
        print(s)
        if s != "":
            clean_L.append(s)
            
    clean_L.pop(0)
    nested_L = []
    for pair in clean_L:
    # "apple 120"
        new_pair = pair.split(" ")
    # ["apple", "120]
        nested_L.append(new_pair)
    
    print(nested_L)
    return nested_L


#clean_L = ["5", "apple 120", "banana 200", "apple 150]

#clean_L = ["apple 120", "banana 200", "apple 150"]


# nested_L = [["apple", "120"], ["banana", "200"], ["apple", "150"]]
    
nested_L = [['apple', '120'], ['banana', '200'], ['apple', '150']]
    
def solution(nested_L):

    dictionary = {}
    
    for pair in nested_L:
        dictionary[pair[0]] = []
    
    for pair in nested_L:
        
        dictionary[pair[0]].append(int(pair[1]))
    
    #dictionary = {'apple': 120, 150, 'banana': 200)
    
    end_list = []
    for k, v in sorted(dictionary.items()):
        #k = apple, v = 120, 150
        max_v = max(v)
        mean_v = sum(v)/len(v)
        min_v = min(v)

        end_list.append([k, max_v, mean_v, min_v])
    
    return end_list
