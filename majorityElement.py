# Given an array nums of size n, return the majority element. The # majority element is the element that appears more than ⌊n / 2 ...
# ex: Input: nums = [2,2,1,1,1,2,2]
#     Output: 2

class Solution:
  def findMajorityElement(self, nums:list) -> list:
    
    auxlist = []
    counterlist = []
    n = len(nums)

    for i in nums:
      auxlist.append(i)
      if i in auxlist:
        pass

    print(auxlist)




nums = [2,2,1,1,1,2,2]
a = Solution()
a.findMajorityElement(nums)