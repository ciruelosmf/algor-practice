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
    res2 = [[1],[1],[1]]

    print(len(res2[-1]), "res2",res2)
    for i in range(numRows-1):
      temp = [0] + res[-1] + [0]
      print(temp, len(res[-1]), "len")
      row = []
      for j in range(len(res[-1]) + 1):
        row.append(temp[j] + temp[j+1])
      res.append(row)
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
