MINIMUM DISTANCE TO THE FARTHEST NODE

import math

def solution(edges):
    
    if len(edges) == 1:
        return 1
    
    new_list = []
    edges_c = edges[:]
    
    for i in range(len(edges_c)):
        value = min(edges_c)
        new_list.append(value)
        edges_c.remove(value)
    
    distance = 1
    for i in range(len(new_list)-1, 0, -1):
        if new_list[i][0] == new_list[i-1][1]:
            if new_list[i][0] == new_list[i-1][1]:
                new_list[i-1][1] = new_list[i][1]
                new_list.remove(new_list[i])
                distance += 1
        else:
            new_list.remove(new_list[i-1])
    
    shortest_d = math.ceil(distance/2) 
    return shortest_d
