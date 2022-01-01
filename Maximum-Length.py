"""

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

[ "cos", "meto", "log", "ia" ]

cosia
metoia -> s -> maximum possible length
logia

len(s) = 6

"""


class Solution:
    def maxLength(self, arr):
      d = {}
      res, maxCount = 0, 0
      aux_s = ""
      counter = 1
      for e in arr:
        for c in e:
          print(c)
          if counter == len(arr):
            counter = len(arr)-2
            
          if c in e[counter]:
            aux_s += c 
          else:
            counter += 1
      print(aux_s)

            



      for i in arr:
        for c in i:
          if c in d:
            d[c] += 1
            print(4)
          else:
            d[c] = 1
            print(123123123123)

      print(d)


array = ["cos", "meto", "log", "ia"]

aa = Solution()
aa.maxLength(array)


