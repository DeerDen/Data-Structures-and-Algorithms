class Node(object):
    
    def __init__(self, val): # doubly linked list
        self.val = val
        self.next = None # points to nothing initially
        self.prev = None

    def get_val(self): # return current value 
        return self.val

    def get_next(self): # return next value
        return self.next.val

    def get_prev(self): # return previous value
        return self.prev

    def traverse(self): # traverse through the full list
        node = self
        while node != None:
            print(node.val)
            node = node.next
        return

    # node1.traverse() - to traverse forward

    def traverse_back(self): # traverse backwards through the list
        node = self
        while node != None:
            print(node.val)
            node = node.prev
        return

    # node6.traverse_back() - to traverse backwards

    
if __name__ == "__main__":
  
    # init linkedlist of 6 nodes in ascending order
    node1 = Node(2)
    node2 = Node(12)
    node3 = Node(23)
    node4 = Node(36)
    node5 = Node(47)
    node6 = Node(51)
    
    # Connect nodes 
    node1.next = node2 # node1 - head node

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    node3.next = node4

    node4.prev = node3
    node4.next = node5

    node5.prev = node4
    node5.next = node6

    node6.prev = node5

    # Final linkedlist looks like
    # 2 (head) <=> 12 <=> 23 <=> 36 <=> 47 <=> 51
    
    # Run this file to create the linkedlist
