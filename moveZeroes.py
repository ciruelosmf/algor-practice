"""

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

**Input**:    nums   =   [0,1,0,3,12]
**Output**:   nums   =   [1,3,12,0,0]

"""

class Solution:
    def move_zeroes(self, array):

      len_array = len(array)

      for e in array:
        if 0 == e:
          array.append(e)

      print(array)








nums = [0,1,0,3,12]

aa = Solution()
aa.move_zeroes(nums)