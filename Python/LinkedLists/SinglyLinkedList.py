class Node(object):
    
    def __init__(self, val): # note this is a singly linked list
        self.val = val
        self.next = None # point to nothing initially

    def get_val(self): # return current value 
        return self.val

    def get_next(self): # return next value
        return self.next.val

    def traverse(self): # traverse through the full list
        node = self
        while node != None: # print val and increment node
            print(node.val)
            node = node.next
        return 
    
if __name__ == "__main__":
    
    # init linkedlist of 6 nodes in ascending order
    node1 = Node(3)
    node2 = Node(14)
    node3 = Node(25)
    node4 = Node(32)
    node5 = Node(50)
    node6 = Node(61)
    
    # connect nodes 
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    # the linkedlist looks like
    # 3 -> 14 -> 15 -> 32 -> 50 -> 61
    
    # run this file to initialize the linkedlist
    # call node1.traverse() to see the full linked list traversal
