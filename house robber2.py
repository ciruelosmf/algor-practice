a = [2,3,2,7,6,11]
# [2,3,2,7,6,11][2,3,2,7,6,11]
#temp = max (2 3  m = 3 temp
#temp = max (3 2   m = 3 >> max (temp and m = 3
#temp = max (2 7   m = 7 >> max (temp and m = 7
#temp = max (7 3   m = 7 >> max (temp and m = 7

# [5,2,7]
#temp = 5 m =5
#temp = 7 m =5 >> max (temp and m = 7
#
#
def robb(houses):
    return max(houses[0],robb1(houses[1:]),robb1(houses[:-1]))

def robb1(houses):
    h1, h2 = 0, 0
    for idx in range(len(houses)-1):
        temp = max(houses[idx], houses[idx+1])
        
    for h in houses:
        temp = max(h+h1, h2)
        h1 = h2
        h2 = temp
        print(h1, h2)
        print(temp)
        print(" ")
    return h2


b = robb(a)
print(b,"robb")
