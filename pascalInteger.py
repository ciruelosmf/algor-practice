# given intenger numberRows, return first numberRows of P traigle
# example: numberRows = 5 -> 
#         [ 1 ] 
#         [1, 1]
#       [1, 2, 1]
#      [1, 3, 3, 1]
#    [ 1, 4, 6, 4, 1 ]

res = [[1]]
print(res, "dfg")
class Solution:
  def numberRowsPascalTriang(self, numRows:int):
    res = [[1]]
    res2 = [[1],[1],[1,2,3,4]]

    print(len(res2[-1]), "res2",res2)
    print("")
    
    for i in range(numRows-1):
      print(i, "iiiiiiiiiiiii")
      temp = [0] + res[-1] + [0]
      print(temp, "temp", len(res[-1]), "lenres")
      row = []
      
      for j in range(len(res[-1]) + 1):
        print(j, "jjjjjj")
        row.append(temp[j] + temp[j+1])
        print(temp[j])
        print(temp[j+1])
        print("---")
      
      res.append(row)
      print(res, "ressssssssss")
      print("")
    
    print(res)



"""
class Solution:
  def numberRowsPascalTriang(self, rows:int) -> list:
    rowLists = []
    rows2 = [] 
    aux = 0
    aux2 = 0
    for i in range(rows):
      rowLists.append(1)
      print(rowLists)
      rows2.append(list(rowLists))
    print(rows2, "hola")
"""

a = Solution()
a.numberRowsPascalTriang(6)
