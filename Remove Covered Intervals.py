

a = [[1,3],[3, 6],[2, 8],[2, 6]]
#a.sort()
#ii = [[2,5],8,2]
#d = lambda ii: (ii[0], -ii[1])
#print(d)
#a.sort(key=lambda i: (i[0], -i[1]))

def remove_interval(arrayy):
    arrayy.sort(key=lambda i: (i[0], -i[1]))
    res = [arrayy[0]]
    for l, r in arrayy[1:]:
        print(l, r)
        prev_l, prev_r = res[-1]
        print(res[-1])
        if l >= prev_l and r <= prev_r:
            continue
        res.append([l,r])
        
           
    
remove_interval(a)
