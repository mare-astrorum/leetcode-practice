"""
https://leetcode.com/discuss/interview-question/394347/google-oa-2019-watering-flowers-20
"""




plants = [2, 4, 1, 5, 6, 100]
capacity1 = 5
capacity2 = 7

watering_plants(plants, capacity1, capacity2)

sum(plants)




def watering_plants(plants, capacity1, capacity2):
    
    import copy
    
    refill = 2   # refill starts with 2 because each bucket needs filling

    capacity1_starting = copy.deepcopy(capacity1)
    capacity2_starting = copy.deepcopy(capacity2)
    
    if len(plants) > 1000:
        return "Error, check number of plants"
    for plant in plants:
        if plant > 1000000000:
            return "Error, check plant values"
    
    
    for i in range(len(plants)):
        plant = plants[0]
        
        # When get to the middle, do a final loop.
        
        if len(plants) == 1:
            if capacity2 - plant >= 0:
                return refill
            elif capacity1 - plant >= 0:
                return refill
            elif capacity1 + capacity2 - plant >= 0:
                return refill
            else:
                capacity1 = capacity1_starting
                capacity2 = capacity2_starting
                refill += 1
                if capacity1 - plant >= 0:
                    return refill
                elif capacity2 - plant >= 0:
                    refill += 1
                    return refill
                elif capacity1 + capacity2 - plant >= 0:
                    return refill
                else:
                    refill += 2
                    plant_watered3 = plant - capacity1 - capacity2
                    while plant_watered3 >= capacity1 + capacity2:
                        if plant_watered3 >= capacity1 or capacity2:
                            refill += 1
                        elif plant_watered3 >= capacity1 + capacity2:
                            refill += 2
                        plant_watered3 = plant_watered3 - capacity1 - capacity2
                    return refill
                
        
        

        
        # Start with end value in the list
        
        if capacity2 - plants[-1] >= 0:
            capacity2 = capacity2 - plants[-1]
            plants.pop(-1)
        elif capacity2 - plants[-1] < 0:
            refill += 1
            capacity2 = capacity2_starting
            plant_watered2 = plants[-1] - capacity2
            while plant_watered2 >= capacity2:
                refill += 1
                plant_watered2 = plant_watered2 - capacity2
            plants.pop(-1)
            
        # Continue with the first value in the list 
        
        if capacity1 - plants[0] >= 0:
            capacity1 = capacity1 - plants[0]
            plants.pop(0)
        elif capacity1 - plants[0] < 0:
            refill += 1
            capacity1 = capacity1_starting
            plant_watered1 = plants[0] - capacity1
            while plant_watered1 >= capacity1:
                refill += 1
                plant_watered1 = plant_watered1 - capacity1
            plants.pop(0)
            
            
    
        



#
#        """ Generic function """
        
        
        
#def get_to_middle(i, capacity, capacity_starting):
#        
#    if capacity - plants[i] >= 0:
#        capacity = capacity - plants[0]
#        plants.pop(i)
#    elif capacity - plants[i] < 0:
#        refill += 1
#        capacity = capacity_starting
#        plant_watered = plants[i] - capacity1
#        while plant_watered > capacity:
#            refill += 1
#            plant_watered = plant_watered - capacity
#        plants.pop(i)            
#        
#    return refill