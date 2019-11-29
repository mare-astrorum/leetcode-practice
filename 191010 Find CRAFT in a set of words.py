"""
https://leetcode.com/discuss/interview-question/399689/Google-phone-interview/361641
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