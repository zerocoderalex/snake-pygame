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
print(queue.dequeue())
print(queue.size())