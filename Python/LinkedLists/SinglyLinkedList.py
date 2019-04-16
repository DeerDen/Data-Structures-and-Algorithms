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
    
