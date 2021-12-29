# return greatest value of single element that is the 
# product of 2 elemts within the array
#
# ex: arra = [2,2,4,5,9]
# solution : 4 (2*2 = 4)

array = [2,2,4,5,9]
print("hoal")
lenlist = len(array)
#for j in array: 
# for i in range(lenlist)


class Solution:
  def findGreatestValue(self, listt:list) -> list:
    lst2 = []
    for i in range(0, len(listt)-1):
      for z in range(i, len(listt)):
        lst2.append(listt[z] * listt[i] )
    result = [i for i in lst2 if i in listt]

    if len(listt) != 0:
      print("este es")
    else:
      print(" N/A")

"""
class Solution:
  def findGreatestValue(self, listt:list) -> list:

    lst2 = []
    lenlist = len(listt)
    aux = 0
    greatest = 0
    for i in range(lenlist):
      if i == lenlist-1:
        break
      lst2.append(listt[i] * listt[i+1] )
      aux = aux + 1

    for j in listt: 
      if j in lst2:
        print("this is the greatest", j)
    

    print(lst2)



"""
array = [2,2,4,5,9]
a = Solution()
a.findGreatestValue(array)