class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to pairwise swap elements of a linked list
    def pairwiseSwap(self):
        temp = self.head
 
        # There are no nodes in linked list
        if temp is None:
            return
 
        # Traverse furthethr only if there are at least two
        # left
        while(temp and temp.next):
 
            # If both nodes are same,
            # no need to swap data
            if(temp.data != temp.next.data):
 
                # Swap data of node with its next node's data
                temp.data, temp.next.data = temp.next.data, temp.data
 
            # Move temp by 2 to the next pair
            temp = temp.next.next
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data) # new_node=4 > new_node=3 > new_node=2 
        new_node.next = self.head # new_node.next=None > new_node.next=4(head)
        self.head = new_node # None=4 > self.head=3
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data, "-")
            temp = temp.next
            
 
 
# Driver program
llist = LinkedList()

llist.push(4)
llist.printList()
print (" ")
llist.push(3)
llist.printList()
print (" ")
llist.push(2)
llist.printList()
print (" ")
llist.push(1)
llist.printList()
print (" ")
 
print ("Linked list before calling pairWiseSwap() ")
llist.printList()
 
llist.pairwiseSwap()
 
print ("\nLinked list after calling pairWiseSwap()")
llist.printList()
 
