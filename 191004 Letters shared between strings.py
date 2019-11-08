# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:17:38 2019

@author: A
"""

inp = ["cool","lock","cook"]

word = "cool"
for letter in word:
    for term in inp:
        if letter in term:
            print(letter)

inp.index("lock")


inp = ["bella","label","roller"]

new_seq = []
one_list = []
for term in inp:
    #print(term)
    new_seq = inp[:]
    new_seq.remove(term)
    #print(new_seq)
    for letter in term:
        #print(letter)
        for item in new_seq:
            #print(item)
            if letter in item:
                print(letter)
                one_list.append(letter)

term =      


from collections import Counter    

x = Counter("bella") 

list_word = []
for i in x.elements():
    list_word.append(i)
    
    
c=Counter(inp[0])
for i in range(1,len(inp)):
    c&=Counter(inp[i]) # concept borrowed from [rachit's solution](https://leetcode.com/problems/find-common-characters/discuss/394501/Python-Simple-Solution)
    """
    elements() Return an iterator over elements repeating each as many times 
    as its count. Elements are returned in arbitrary order. If an element’s 
    count is less than one, elements() will ignore it.
    """
print (c.elements())