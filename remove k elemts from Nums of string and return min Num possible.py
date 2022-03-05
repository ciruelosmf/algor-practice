a = "1432219"
k = 3


def remove_k_elemts(stringg, k_int):
    stack = []
    for e in stringg:
        while k_int > 0 and stack and stack[-1] > e:
            k_int -= 1
            stack.pop()
        stack.append(e)
        print(stack,1)
    print(stack,2)
    stack = stack[:len(stringg) - k_int]
    print(stack,3)
    res = "".join(stack)
    print(res)
        
remove_k_elemts(a, k)
