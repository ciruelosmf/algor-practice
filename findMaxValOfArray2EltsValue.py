# return greatest value of single element that is the product of 2 elemts within the array
# ex: arra = [2,2,4,5,9]
# solution : 2 (2*2 = 4)

print("hoal")

class Solution:
  def findMaxValue(self, listt:list, k: float) -> list:

    lst2 = []
    lenlist = len(listt)
    aux = 0
    for i in range(k):
      lst2.append(listt[lenlist-k+aux])
      aux = aux + 1
    for i in range(lenlist-k):
      lst2.append(listt[i])

    print(lst2)