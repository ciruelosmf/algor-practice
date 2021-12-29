# given intenger numberRows, return first row of P traigle
# example: numberRows = 5 -> 
#        [1] 
#       [1, 1],
#      [1, 2, 1], 
#     [1, 3, 3, 1]
#    [1, 4, 6, 4, 1]

class Solution:
  def numberRowsPascalTriang(self, rows:int) -> list:
    rows = []
    rows2 = [] 
    aux = 0
    aux2 = 0
    for i in range(0, len(listt)-1):
      for z in range(i, len(listt)):
        lst2.append(listt[z] * listt[i] )
    result = [i for i in lst2 if i in listt]
    print(lst2)
    if len(result) != 0:
      print("este es", max(result))
    else:
      print(" N/A")
