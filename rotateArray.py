# Rotate Array - Leetcode 189 - Python
# given array, rotate to right by K steps, K non negative

print("hoal")
class Solution:
  def rotate(self, listt:list, k: float) -> list:

    lst2 = []
    lenlist = len(listt)
    aux = 0
    for i in range(k):
      lst2.append(listt[lenlist-k+aux])
      aux = aux + 1
    for i in range(lenlist-k):
      lst2.append(listt[i])

    print(lst2)



l = [1,2,3,4,5,6,7,5,6,7,2,3,45,44]
a = Solution()
a.rotate(l, 3)

