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
