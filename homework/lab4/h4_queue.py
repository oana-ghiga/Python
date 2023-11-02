# with a queue you add elements to the end of the list and remove elements from the beginning of the list so basically first in first out and last always changes
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0) #compared to the stack i added a 0 here to pop the first element
        return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

#put elements in
q = Queue()
q.push('a')
q.push('b')
q.push('c')

print(q.peek())  # Output: 'a'

print(q.pop())  # Output: 'a'

print(q.peek())  # Output: 'b'

print(q.pop())  # Output: 'b'
print(q.pop())  # Output: 'c'

print(q.pop())  # Output: None
print(q.peek())  # Output: None
