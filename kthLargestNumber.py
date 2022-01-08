"""
You are given an array of strings nums and an integer k. Each
string in nums represents an integer without leading zeros.
Return the string that represents the kth largest integer in nums.
Note: Duplicate numbers should be counted distinctly. For example,
if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

Example 1:
Input: nums = ["3","6","7","10"], k = 4
Output: "3"
Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3".

Example 2:
Input: nums = ["2","21","12","1"], k = 3
Output: "2"
Explanation:
The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
The 3rd largest integer in nums is "2".
"""

import heapq as heap

class Solution:
    def kthLargestNumber(self, nums, k):
      maxHeap = [-int(n) for n in nums]
      heap.heapify(maxHeap)

      while k > 1:
        heapq.heappop(maxHeap)
        k -= 1
      return str(-maxHeap[0])



    """
        aux_array = []
        len_nums = len(nums)
        for e in nums:
            aux_array.append(int(e))
            print(e)
        array_max_num = max(aux_array)
        array_min_num = min(aux_array)
        for e in aux_array:
            if len_nums == k:
                print("largest integer in nums is", array_min_num)
                break
            elif e > aux_array[len_nums-k]:
                print("asd",len_nums-k )

                
        print("") 
        print(array_min_num, array_max_num)        
            
        #val = [ int(x) for x in nums ] 
        #val.sort(reverse=True)
        #return str(val[k-1])
      """
nums = ["3","6","7","10"]
k = 3

aa = Solution()
aa.kthLargestNumber(nums, k)
