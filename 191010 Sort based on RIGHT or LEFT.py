# {a, b, "right"} --> a is to the right of b
# {c,b, "right"} --> c is to the right of b
# {b,a, "left"} --> b is to the left of a

L1 = ["a", "b", "right"]
L2 = ["c", "b", "right"]
L3 = ["b", "c", "left"]

L_all= [L1, L2, L3]



def left_right_list(L_all):
    
    result_l_right = []
    result_l_left = []

    for L in L_all:
        print(L)
        num = L.count("right")
        print(num)
        if num == 1:
            result_l_right.append(L[1])
            print(result_l_right)
        else:
            result_l_left.append(L[0])
            print(result_l_left)
    
    return result_l_left + result_l_right

