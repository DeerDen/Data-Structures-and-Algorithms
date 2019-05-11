class Stack(object):
    #  note: stacks are LIFO -> Last in First out
    # Python List complexity -> https://wiki.python.org/moin/TimeComplexity
    
    def __init__(self):
        self.stack = []

    def size(self):
        # O(1) for len of list
        return len(self.stack) 

    def is_empty(self):
        return self.size() == 0
        
    def push(self, val): # Add Element to top stack
        # O(1) for list append
        self.stack.append(val)
            
    def peek(self): # View top of stack
        if self.is_empty():
            return 'Empty Stack'
        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            return 'Empty Stack'
        # O(1) for list pop
        return self.stack.pop()

if __name__ == "__main__":
    # To init stack on run
    stack = Stack()
    stack.push("First")
    stack.push("Second")
    stack.push("Third")