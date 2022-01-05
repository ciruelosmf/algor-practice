"""
Given a non-empty array of integers nums, every element
appears twice except for one. Find that single one.
You must implement a solution with a linear runtime
complexity and use only constant extra space.

**Input**:    nums = [2,2,1]
**Output**:   1
"""

class Solution:
    def singleNumber(self, nums) -> int:
        #d = {}
        #target = 0
        #aux = 1
        #for e in nums:
            #if e in d:
                #d[e] += 1
                
            #else:
                #d[e] = 1
                #target = e

        #print(d)
        #print(target)

        # xor
        res = 0
        for num in nums:
            print("")
            print(bin(res), "no xor")
            res = res ^ num
            print(bin(res))
        return res


nums = [4,1,2,1,2]

aa = Solution()
aa.singleNumber(nums)
