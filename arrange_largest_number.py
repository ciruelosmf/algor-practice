array_to_test = [1,17,8,3,21]
array_to_test2 = [8,3,21,17,1]


def arrange_largest_number(arrayy):#, l=[]):
    #arrayy.sort(key=lambda i: -int(str(i)[0]))
    for i, n in enumerate(arrayy):
        arrayy[i] = str(n)
    print(arrayy)
    import functools
    def compare(n1, n2):
        
        if n1 + n2 > n2 + n1:
            print(n1, n2,n1+n2,n2+n1)
            print(-1)
            return -1
        else:
            print(1)
            return 1
    arrayy = sorted(arrayy, key=functools.cmp_to_key(compare))
    return str(int("".join(arrayy)))
                    

    print(arrayy)

def arrange_largest_number2(arrayy):#, l=[]):
    #arrayy.sort(key=lambda i: -int(str(i)[0]))
    ee = sorted(arrayy, key = lambda i: -(int(str(i)[0])))

    return ee

print(array_to_test)
aaa = arrange_largest_number(array_to_test)
print(aaa)
