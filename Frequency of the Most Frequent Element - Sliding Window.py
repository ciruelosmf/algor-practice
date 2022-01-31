array_to_check = [1,1,1,2,2,4]
k_operations = 12
array_to_check3 = [1,4,8,13, 7]
array_to_check4 = [3,9,6]
#####################################




def Frequency_of_Most_Frequent_Element(arrayy, k):
    arrayy.sort()
    l, r = 0, 0
    res, total = 0, 0

    while r < len(arrayy):
        total += arrayy[r]
        print(total, "total")
        print(r , "(r)")
        print(l , "l ")

        while arrayy[r] * (r - l +1)> total + k:
            print((r - l +1), "(r - l +1)")
            total -= arrayy[l]
            l += 1
        res = max(res, r-l+1)
        print(res, "res")
        print(" ")
        r +=1
    return res



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
        
    
#####################################
    
b = Frequency_of_Most_Frequent_Element(array_to_check3, k_operations)
print(array_to_check3)
print( "Frequency_Most_Frequent_Element is ", b)
