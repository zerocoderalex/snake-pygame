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









