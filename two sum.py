nums = [2,1,7,3]
target  = 8

print(3.16*3.16)

from math import sqrt
import heapq



def two_sum(nums, target_to_discover):
    
    prev_map = {}
    for i, n in enumerate(nums):
        diff = target_to_discover - n
        if diff in prev_map:
            return [nums[diff], i]
        prev_map[n] = i

                
    return



def two_sum_big_bigO(nums, target_to_discover):
    
    minHeapa = []
    for i in range(len(nums)-1):
        
        for ii in range(i+1, len(nums)):
            print(i+1, len(nums))
            
            if nums[i] + nums[ii] == target_to_discover:
                
                return [i, ii]
    print("no se puede")




r = two_sum(nums, target)
print(r)

