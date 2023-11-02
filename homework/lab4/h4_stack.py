#with a stack you add elements on top of each other and you can only remove the top element so basically the first in last out and first always changes
class Stack:
    def __init__(self): # constructor
        self.stack = [] # create an empty list for the stack

    def push(self, item):
        self.stack.append(item) # push basically does the same thing as append

    def pop(self):
        if not self.is_empty():
            return self.stack.pop() # using pop to pop?
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1] # -1 is the last element in the list if it would've been 0 it would show the first element
        return None

    def is_empty(self):
        return len(self.stack) == 0



# populate the stack
s = Stack()
s.push('a')
s.push('b')
s.push('c')

# peek-a-boo at the top
print(s.peek())  # Output: 'c'

# pop it out
print(s.pop())  # Output: 'c'

# show the element at the top of the stack
print(s.peek())  # Output: 'b'

# pop when elements are in the stack
print(s.pop())  # Output: 'b'
print(s.pop())  # Output: 'a'

# pop and peek for empty
print(s.pop())  # Output: None
print(s.peek())  # Output: None
