e = [9,12,7,8,1,5]
sdf = {"1","2","3","4"}
print(len(sdf))
import random
ee = []
for n in range(5577565):
    ee.append(random.randint(1,16)) 

# [1,12,7,8,1,5]
kk = 6




def first_ocurrence_of_nbr_greater_k(nums_Array, k_int):

    asd = []

    for idx in range(1,len(nums_Array)-1):    
        if nums_Array[idx] > k_int:
            asd.append(nums_Array[idx])
            
    return min(asd)

t = first_ocurrence_of_nbr_greater_k(ee, kk)
print(t, "_---")

  
