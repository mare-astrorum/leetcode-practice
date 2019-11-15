"""
https://leetcode.com/problems/rotting-oranges/
"""

ex1 = [[2,1,1],
       [1,1,0],
       [0,1,1]]

#len(ex1)
#turn = 0
#cycles = len(ex1)
#while True:
#    
#locx = []
#locy = []    
len(ex1)
for index_x, i in enumerate(ex1):
    print(index_x, i)
    for index_y, j in enumerate(i):
        print(index_y, j)
        if j == 2:
            locationx = index_x + 1
            print(locationx)
            locationy = index_y + 1
            print(locationy)
            print(ex1[index_x][locationy])
            if ex1[index_x][locationy] == 1:
                    ex1[index_x][locationy] = 2
        else:
            break
            if ex1[index_y][locationx] == 1:
                    ex1[index_x][locationy] = 2
#
#            ex1[locationx+1][locationy] = 2
#            ex1[locationx][locationy+1] = 2
            print(ex1)
            new_rot_x = ex1[locationx+1][locationy]
            new_rot_y = ex1[locationx][locationy+1]
#            elif turn < cycles:
                    turn +=1

                     


[[2, 2, 1], 
 [2, 2, 0], 
 [2, 1, 1]]  
