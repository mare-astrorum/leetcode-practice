"""
https://leetcode.com/problems/merge-intervals/
"""

# Incomplete


intervals = [[1,3], [2,4], [9,12], [5,7], [11,15]]
lis = [] 
for i in range(len(intervals)-1):
     #0
     if intervals[i+1][0] in range(intervals[i][0], intervals[i][1]) and intervals[i][1] in range(intervals[i+1][0], intervals[i+1][1]):
         print(intervals[i], intervals[i+1])
         new_interval = [intervals[i][0], intervals[i+1][1]]
         lis.append(new_interval)
intervals.pop(i+1)
intervals.pop(i)
intervals.insert(i, new_interval)
print(intervals)


sort(intervals)        

new_l = []
    start_v = 0
    for item in intervals:
        if item >
 