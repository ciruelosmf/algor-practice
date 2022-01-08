"""
Given an integer array --nums--, find the contiguous
subarray (containing at least one number)
which has the largest --sum-- and return its --sum--.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

"""

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [4,-1,2,1,-5,4]


class Solution2:
    def maxSubArray(self, nums):
      max_sum = nums[0]
      curren_sum = 0
      for i in nums:
        if curren_sum < 0:
          curren_sum = 0
        curren_sum += i
        max_sum = max(max_sum, curren_sum)
      print(max_sum)

class Solution:
    def maxSubArray(self, nums):
      sum_nums = sum(nums)
      largest_possible_sum = 0
      subarray = []
      aux_array = []

      for index in range(len(nums)+1):
        for index1 in range(index+1, len(nums)+1):
          sub = nums[index:index1] 
          aux_array.append(sub)
          print(aux_array)
          print("")
          sumsub = sum(sub)
          print(sumsub,"sumsub")
          if sumsub > largest_possible_sum:
            largest_possible_sum = sumsub
            print(sub, "este es sub")
      print(aux_array)
      print(largest_possible_sum)
        
        #subarray.append(nums[index])
        #largest_possible_sum = sum(subarray)
        #print(largest_possible_sum, "largest_possible_sum")
        #aux_array.append(largest_possible_sum)
        
        #if sum(subarray) > sum_nums or sum(subarray) > largest_possible_sum:
          #print(1,subarray)
        #print(aux_array)


      
      #print(sum(nums))




#aa = Solution()
#aa.maxSubArray(nums)
aa2 = Solution2()
aa2.maxSubArray(nums)













