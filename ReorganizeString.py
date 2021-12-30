# rearreange strings S so that any 2 adyacent chars are 
# not the same, otherwise  return ""
# ex: aab -> aba 
# ex2: aaab -> ""




class Solution:
    def reorganizeString(self, s: str) -> str:
      newString = ""
      noString = ""
      aux = []
      for i in s:
        aux.append(i)
        print(i)
      print(aux)

a = Solution()
s = "aab"
a.reorganizeString(s)