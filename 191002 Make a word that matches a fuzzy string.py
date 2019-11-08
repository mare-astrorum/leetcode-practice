# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:10:44 2019

@author: A
"""

Slist = []

D = ["able", "ale", "apple", "bale", "kangaroo"]


S = "abppplee"
Slist = []
indexl = []

index = list(range(len(S)))
for letter in S:
    Slist.append(letter)

    
new_word = []    
word = "able"
wordindex = list(range(len(word)))

for i in word:    
    if i in Slist:
        print(Slist.index(i))
        print(word.index(i))
        if Slist.index(i) <= word.index(i):
            new_word.append(i)
            Slist.remove(i)
        else:
            print("ERROR")
            break
        
    
