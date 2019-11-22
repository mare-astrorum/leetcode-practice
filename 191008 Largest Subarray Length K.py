"""
https://leetcode.com/discuss/interview-question/352459/
"""


A = [4, 1, 4, 3, 2, 5, 6]
K = 5


# Version 1

# Find all subarrays

def all_subarrays(A, K):
    all_subarrays = []
    for i in range(len(A)-(K-1)): #1
        arr = A[i:i+K] #[1, 4, 3, 5]
        all_subarrays.append(arr)
    return all_subarrays # [[1, 4, 3, 5], [4, 3, 2, 5], [3, 2, 5, 6]]

# Find max one 

def solution(A, K):
    
    return max(all_subarrays(A, K))



# Version 2

def lesser_array(X, Y):
    for ind, num in enumerate(X):
        if num < Y[ind]:
            return X
        if num > Y[ind]:
            return Y

i = 0
all_subarrays

len(A)-(K-1)


def compare_subarrays(all_subarrays):
    for i in range(len(all_subarrays)-1):
        print(i)
        X = all_subarrays[0]
        print(X)
        Y = all_subarrays[1]
        print(Y)
        les_array = lesser_array(X, Y)
        print("---")
        all_subarrays.remove(les_array)
        print(all_subarrays)
        print("***")

    return all_subarrays


def final_function(A, K):

    all_subarr = all_subarrays(A, K)

    answer_l = compare_subarrays(all_subarr)
    answer = answer_l[0]
    
    

    return answer

final_function(A, K)


max(all_subarrays)
test = [[1,2,3],[1,3,2]]
max(test)
