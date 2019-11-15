
"""
https://techdevguide.withgoogle.com/resources/volume-of-water/#!
"""
import matplotlib.pyplot as plt


terrain = [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]

len(terrain)
valleys = []
    
index = 0
for i in terrain:
    #print(i)
    next_block = terrain[index+1]
    if i >= next_block:
        valley = i - next_block
        valleys.append(valley)
        
        
#        print(index)
#        print("yes")
    index+=1
    

index = 0
for i in terrain:
    #print(i)
    next_block = terrain[index+1]
    difference = next_block - i
    valleys.append(difference)
    index+=1