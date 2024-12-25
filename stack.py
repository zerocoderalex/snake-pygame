class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

stack = Stack()

print(stack.is_empty())
stack.push(3)
stack.push(2)
stack.push(1)
print(stack.is_empty())
print(stack.peek())

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append( item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

queue = Queue()

print(queue.is_empty())
queue.enqueue(33)
queue.enqueue(22)
queue.enqueue(11)
print(queue.size())
queue.dequeue()
print(queue.size())







