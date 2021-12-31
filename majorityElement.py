# Given an array nums of size n, return the majority element. The # majority element is the element that appears more than ⌊n / 2 ...
# ex: Input: nums = [2,2,1,1,1,2,2]
#     Output: 2

class Solution:
  def findMajorityElement(self, nums:list) -> list:
    
    d = {}
    auxlist = []
    counterlist = []
    n = len(nums)

    for i in nums:
      if i in d:
        d[i] += 1
        print(4)
      else:
        d[i] = 1
        print(123123123123)
      auxlist.append(i)
      #if i in auxlist:
        #d[i] += 1
        #pass

    print(auxlist)
    print(d)


class Solution2:
  def findMajorityElement(self, nums:list) -> list:
    
    d = {}
    res, maxCount = 0, 0
    counterlist = []
   

    for i in nums:
      if i in d:
        d[i] = 1 + count.get(n,0)
        res = i if count[n] > maxCount else res
        maxCount = max(count[n], maxCount)
    print(res)

nums = [2,2,1,1,1,2,2]
a = Solution()
a.findMajorityElement(nums)

nums2 = [2,2,1,1,1,2,2]
aa = Solution2()
aa.findMajorityElement(nums2)