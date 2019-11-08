WATERING PLANTS

plants = [2, 4, 5, 1, 2]
capacity1 = 5
capacity2 = 7

refill = 2

1.  5-2 = 3     2. 3-4 = -1 ==> refill > 5-2 = 1
    7-2 = 5        5-1 = 4  

3.  1-5 or 6-5

#class Solution:
    
def watering_plants(plants, capacity1, capacity2):   

    import copy       

    refill = 2
    capacity1_starting = copy.deepcopy(capacity1)
    capacity2_starting = copy.deepcopy(capacity2)

    for i in range(len(plants)):
        
        if len(plants) == 1:
        
            if capacity2 - plants[0] >= 0: 
                return refill
            elif capacity1 - plants[0] >= 0: 
                return refill
            elif capacity1 + capacity2 - plants[0] >= 0:
                return refill
            else:
                refill += 1
                return refill


        if capacity1 - plants[0] >= 0: #5-2, 3-4
            capacity1 = capacity1 - plants[0] #0
            plants.pop(0)
        elif capacity1 - plants[0] < 0: 
            refill +=1
            capacity1 = capacity1_starting
            capacity1 = capacity1 - plants[0]
            plants.pop(0)#[4, 5, 1]

        
        if len(plants) == 1:
            continue

        if capacity2 - plants[-1] >= 0:
            capacity2 = capacity2 - plants[-1] #7-2, 5-1
            plants.pop(-1) #[2,4,5,1], [4, 5]
        elif capacity2 - plants[-1] < 0: 
            refill +=1
            capacity2 = capacity2_starting
            capacity2 = capacity2 - plants[-1]
            plants.pop(-1) #[4, 5, 1]

        
