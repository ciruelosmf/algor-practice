a = [2,3,2]





def robb(houses):
    h1, h2 = 0, 0
    
    for h in houses:
        
        temp = max(h+h1, h2)
        h1 = h2
        h2 = temp
        print(h1, h2)
        print(temp)
        print(" ")


b = robb(a)
print(b,"robb")
