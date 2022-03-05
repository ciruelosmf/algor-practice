lstt = [1,2,3,4,5]
l = 2
r = 4  # [1,4,3,2,5]
# [1,2,3,4,5,6,7,8,9]
# [1,7,6,5,4,3,2,8,9,10] 2 7
# 2-7  6-3  5-4

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # 1) reach node at position "left"
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
        
        # Now cur="left", leftPrev="node before left"
        # 2) reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext
            
        # 3) Update pointers
        leftPrev.next.next = cur # cur is node after "right"
        leftPrev.next = prev     # prev is "right"
        return dummy.
