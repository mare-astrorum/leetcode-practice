# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:57:04 2019

@author: A
"""

import string
abc = list(string.ascii_lowercase)
mc = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

word = "gin"
words = ["gin", "zen", "gig", "msg"]
morse_words = []
morse_word = ""

for word in words:
    morse_word = ""
    for i in word:
        ind = abc.index(i)
        morse_letter = mc[ind]
        morse_word = morse_word + morse_letter
    morse_words.append(morse_word)
    
morse_words
len(set(morse_words))



class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)
