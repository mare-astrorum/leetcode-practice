"""
https://leetcode.com/problems/unique-morse-code-words/
"""

import string
abc = list(string.ascii_lowercase)
mc = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]



class Solution:
    def uniqueMorseRepresentations(self, words):
        morse_words = []
        for word in words: 
            morse_word = ""
            for i in word:
                ind = abc.index(i)
                morse_letter = mc[ind]
                morse_word = morse_word + morse_letter
            morse_words.append(morse_word)
    
        return len(set(morse_words))
        



class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)
