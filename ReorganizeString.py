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
        print(i,1)

        #for k in range(len(aux)):
          #if aux[k] == aux[k-1]:
            #print(234, k)
            #print(aux[k], "aux k")
        
        aux.append(i)
        print(i,len(aux), "len")

      print("")
      print(aux)
      for k in range(len(aux)-1):
        if aux[k] == aux[k+1]:
          aux[k] = aux[k-1]
      print(aux)

a = Solution()
s = "aab"
a.reorganizeString(s)