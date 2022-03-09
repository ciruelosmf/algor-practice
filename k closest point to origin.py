points = [2,7,11,15]

print(3.16*3.16)

from math import sqrt
import heapq



def k_closest_pnt_to_origin(points_list):
    minHeapa = []
    
    for x, y in points_list:

        dist = (x**2) + (y**2)
        minHeapa.append([dist, x, y])
        
    print(minHeapa)
    print("")
    heapq.heapify(minHeapa)
    
    print(minHeapa)
    res = []
    dist, x, y = heapq.heappop(minHeapa)
    res.append([x,y])
    

    
    return res




r = k_closest_pnt_to_origin(points)
print(r)

