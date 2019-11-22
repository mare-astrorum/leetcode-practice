"""
https://leetcode.com/discuss/interview-question/352458/Google-or-OA-Fall-Internship-2019-or-Compare-Strings
"""

import re

str1 = "aaabcdfwefw, qqqabc, bd"
str2 = "a, a"


def find_length(word):

    word_min = min(word)  #==> a
    no_min = re.findall(word_min, word)
    min_length = len(no_min)
    
    return min_length


def compare_strings(str1, str2):
       
    
    A = str1.split()
    B = str2.split()
    


    list_numbers_A = []
    list_numbers_B = []

    for word in A:

        word_length = find_length(word)
        list_numbers_A.append(word_length) # ==> 1 2 1


    for word in B:

        word_length = find_length(word)
        list_numbers_B.append(word_length) # ==> 3 2



    result = []
    for num in list_numbers_B:
        total_num = 0
       #1
        for a in list_numbers_A:
        # 3
            if num > a:
                total_num += 1  # total_number = 3
                print(total_num)
            elif num < a:
                total_num += 0
        result.append(total_num)

    print(result)
    return result
