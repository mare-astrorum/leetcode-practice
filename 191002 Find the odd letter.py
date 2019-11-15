"""

Find the extra character in one of the words, word order doesn't matter

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

