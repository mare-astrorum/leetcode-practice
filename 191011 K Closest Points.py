"""
https://leetcode.com/problems/k-closest-points-to-origin/
"""

points = [[3,3],[5,-1],[-2,4],[3,14]]
K = 2

import math

    def kClosest(points, K):
        
        total_list = []
        ans = []
        
        # Find the distance
        
        for pair in points:
            response = math.sqrt(pair[0]**2 + pair[1]**2)
            total_list.append(response)
        
        # Find minimum values
            
        for i in range(K):
            min_v = min(total_list)
            index = total_list.index(min_v)
            p = points[index]
            ans.append(p)
            total_list.pop(index)
            points.pop(index)
            
        return ans
    
