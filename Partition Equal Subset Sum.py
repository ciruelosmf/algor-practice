array_to_check2 =[1, 1, 1, 15]
array_to_check = [1,5,11,5]

dpv = set()
dpv2 = set()
dpv.add(0)
dpv2.add(5)
print(dpv)
dpv.add(5)
print(dpv)
dpv.add(35)
dpv= dpv2
print(dpv)

###############--------###################### [1, 5, 5, 5 ,6, 11, 11]
###############--------######################   [1, 5, 5, 11]  [1, 1, 1, 15]


def Partition_Equal_Subset_Sum(arrayy):
    #arrayy.sort()
    dp = set()
    dp.add(0)
    target = sum(arrayy) // 2
    for i in range(len(arrayy)-1,-1,-1):
        nextDP = set()
        print(dp)
        for t in dp:
            print(t,"ttttttttttt ")
            #if(t+arrayy[i]) == target:
                #return True
            nextDP.add(t+arrayy[i])
            nextDP.add(t)
            print(nextDP,"nextDP||||||||| ",t+arrayy[i])
        
        dp = nextDP
        print(dp,"dp--------- ")
    return True if target in dp else False



###############--------######################
###############--------######################


def Frequency_of_Most_Frequent_Element_notcorrect(arrayy, k):
    maxim_possibl_frequency = 0
    max_elemtn_of_array = max(arrayy)
    k_pointer = k

    while k_pointer >= 0:
        for e in arrayy:
            if e <= max_elemtn_of_array and e != max_elemtn_of_array:
                maxim_possibl_frequency += 1
            k_pointer -= 1
    return maxim_possibl_frequency
        
    
###############--------######################
###############--------######################
    
b = Partition_Equal_Subset_Sum(array_to_check)
print(array_to_check)
print( "Frequency_Most_Frequent_Element is ", b)
