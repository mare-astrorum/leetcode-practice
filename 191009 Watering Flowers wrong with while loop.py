#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:09:52 2019

@author: ai
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:21:42 2019

@author: ai
"""

import copy

plants = [2, 4, 5]

capacity1 = 1

capacity2 = 1

refill = 2
capacity1_starting = copy.deepcopy(capacity1)
capacity2_starting = copy.deepcopy(capacity2)

1.

5-2 = 3
7-2 = 5

2. 

3-4 = -1 ==> refill
5-1 = 6

3. 

5-5 or 6-5

plants = [5]
import copy

#Class Solution:
    
def watering_plants(plants, capacity1, capacity2):


    if capacity1 == 0 or capacity2 == 0:
#        return "Error, check bucket volume"
        print("Error, check bucket volume")
        break
    if len(plants) > 1000 or len(plants) < 1:
#        return "Error, check amount of plants"
        print("Error, check amount of plants")
        break
    for plant in plants:
        if plant > 1000000:
#            return "Error, check plant value"   
            print("Error, check plant value")    
            break

    



#plants = [2, 4, 5, 1, 2]

    for i in range(len(plants)):
        plant = plants[0]
        print(plants)
        print(plant)
        #[0] 5
        if len(plants) == 1:
            print("List is 1")
            print(plant)
            if capacity2 - plant >= 0: 
                print(refill)
                break
                #return refill
            elif capacity1 - plant >= 0: 

                print(refill)
                break
                #return refill
            elif capacity1 + capacity2 - plant >= 0:
                print(refill)
                break
                #return refill
            else:
#                print("Need to work out the amount of w")
                
#                else:
                print("Final Loop")
                refill += 1
                capacity2 = capacity2_starting
                capacity1 = capacity1_starting
                if capacity2 - plant >= 0: 
                    print(refill)
                elif capacity1 - plant >= 0: 
                    refill += 1
                    print(refill)
                elif capacity1 + capacity2 - plant >= 0:
                    print(refill)
                else:
                    print("Enter tricky loop")
                    print(refill)
                    refill += 2
                    plant_watered3 = plants[-1] - capacity2 - capacity1
                    print(plant_watered3)
                    while plant_watered3 >= capacity2 + capacity1:
                        if plant_watered3 > capacity2 or plant_watered3 > capacity1:
                            print("Need more refills in the same cycle 3 from individual buckets")
                            refill +=1
                        elif plant_watered3 > capacity2 + capacity1:
                            refill +=2
                        print(refill)
                        plant_watered3 = plant_watered3 - capacity2 - capacity1
                    print(plant_watered3)
                    print("Final amount")
                    print(refill)
                break




        if capacity2 - plants[-1] >= 0: 
            print(capacity2)
            print("enter loop of end integer and the bucket fits in one go")
            capacity2 = capacity2 - plants[-1] #7-2, 5-1
            plants.pop(-1) 
            print(plants)#[2,4,5,1], [4, 5]
        else:
            print(capacity2)
            print("enter loop of end integer and the bucket needs refill")
            refill +=1
            capacity2 = capacity2_starting
            plant_watered2 = plants[-1] - capacity2
            print(plant_watered2)
            while plant_watered2 >= capacity2:
                print("Need more refills in the same cycle 2")
                refill +=1
                print(refill)
                plant_watered2 = plant_watered2 - capacity2
                print(plant_watered2)
            print("Leaving smaller amount loop 2")
            plants.pop(-1)

            
        if capacity1 - plant >= 0: 
                print(capacity1)
                print("enter loop of front integer and the bucket fits in one go")
                print("larger")
                capacity1 = capacity1 - plant
                print(capacity1)
                plants.pop(0)
        elif capacity1 - plant < 0: 
                print(capacity1)
                print("enter loop of front integer and the bucket needs refill")
                print("smaller")
                refill +=1 
                print(refill)
                capacity1 = capacity1_starting
                print(capacity1)
                plant_watered = plant - capacity1
                print(plant_watered)
                while plant_watered >= capacity1:
                    print("Need more refills in the same cycle 1")
                    refill +=1
                    print(refill)
                    plant_watered = plant_watered - capacity1
                    print(plant_watered)
                print("Leaving smaller amount loop 1")
                plants.pop(0)
                
                    
        print("---")
            











#for i in range(len(plants)):
#    plant = plants[0]
#    print(plants)
#    print(len(plants))
#    print(capacity1 - plant)
#        if capacity1 - plant >= 0: 
#                print("larger")
#                capacity1 = capacity1 - plant
#                print(capacity1)
#                plants.pop(0)
#        elif capacity1 - plant < 0: 
#                print("smaller")
#                refill +=1 
#                print(refill)
#                capacity1 = capacity1_starting
#                print(capacity1)
#                plant_watered = plant - capacity1
#                print(plant_watered)
#                while plant_watered > capacity1:
#                    print("Need more refills in the same cycle")
#                    refill +=1
#                    print(refill)
#                    plant_watered = plant_watered - capacity1
#                    print(plant_watered)
#                print("Leaving smaller amount loop")
#                plants.pop(0)
#                
#                    
#        print("---")
    
    



            
watering_plants(plants, capacity1, capacity2)
