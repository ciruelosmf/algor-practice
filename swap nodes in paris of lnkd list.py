

class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data) # new_node=4 > new_node=3 > new_node=2 
        new_node.next = self.head # new_node.next=None > new_node.next=4(head)
        self.head = new_node
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data, "-")
            temp = temp.next

llist = LinkedList()
elem = Node(4)
llist.head = elem
g = llist.head
#print(llist.head)

elem2 = Node(3)
llist.head.next = elem2
elem3 = Node(2)
llist.head.next.next = elem3
llist.printList()
"""
a=llist.push(4)
u = a.next
print (" ", u )
llist.printList()
print (" ")
aa=llist.push(3)
llist.printList()
print (" ")
aaa=llist.push(2)
llist.printList()
print (" ")
aaaa=llist.push(1)
llist.printList()
"""


class Solution:
    def swap_pairs(self, heada):
        dummy = Node(0, heada)
        
        # 1) 
        prev, curr = dummy, heada

        # 2) 
        while curr and curr.next:
            next_pair = curr.next.next
            second = curr.next
            
            second.next = curr
            curr.next = next_pair
            prev.next = second
            
            prev = curr
            curr = next_pair

        return dummy.next

f = Solution()
print(llist.head.data)
ff = f.swap_pairs(llist.head)
print(ff)
