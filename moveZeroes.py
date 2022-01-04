"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
**Input**:    nums   =   [0,1,0,3,12]
**Output**:   nums   =   [1,3,12,0,0]
"""

class Solution:
    def move_zeroes(self, array):
        len_array = len(array)
        aux = 0
        aux_array = []

        for e in array:
            array.remove(0)
            array.append(0)


        print(array, "array final")


nums = [0,1,0,3,12,0, 0,7,5,87,3,0,0, 3,12,0, 0,0,3,12,0, 0,7,5,87,3,0,0, 3,12,5,87,5,87,3,0,0,2,3]

aa = Solution()
aa.move_zeroes(nums)
