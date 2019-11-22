'''
https://leetcode.com/discuss/interview-question/396646/google-oa-2020-maximum-number-of-strawberries
'''


# MAXIMUM NUMBER OF STRAWBERRIES

def solution(inp, K):

    sum_list = []
        
    for i in range(len(inp)):
#        First find max value
        value = max(inp) 
        value_index = inp.index(value) 
        sum_list.append(value)
        if sum(sum_list) == K:
            return sum(sum_list)
        if sum(sum_list) < K:
#            Describe end case
            if value_index == len(inp)-1: 
                inp.pop(-1)
                if not inp:
                    return sum(sum_list)
                inp.pop(-1)
#            Describe start case
            elif value_index == 0:
                inp.pop(0)
                inp.pop(0)
            else:
#            Describe other cases
                inp.pop((value_index)+1)
                inp.pop(value_index)
                inp.pop((value_index)-1)
                
        if sum(sum_list) > K:
            sum_list.remove(value)
            inp.pop(value_index)
            if not inp:
                return sum(sum_list)
                  
    return sum(sum_list)