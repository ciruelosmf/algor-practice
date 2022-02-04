#  Given an unsorted integer array nums,
#  return the smallest missing positive integer.
# Input: nums = [3,4,-1,1]
# Output: 2

a = [1,2,0] # output 3
target = len(a)-1





def First_Missing_Positive(arrayy):
    min_default = 1
    aux_set = set()

    for i in range(len(arrayy)):
        print(arrayy[i],"arrayy[i]")
        aux_set.add(arrayy[i])
    print(aux_set)



b = First_Missing_Positive(a)
print(b,"First_Missing_Positive")
