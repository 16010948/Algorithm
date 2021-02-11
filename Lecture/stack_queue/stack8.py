class Stack:
    def __init__(self):
        self.data = []

    def pop(self):
        if self.size() == 0:
            raise Exception("스택이 비어있습니다")
        return self.data.pop()

    def push(self, item):
        self.data.append(item)

    def peek(self):
        if self.size() == 0:
            raise Exception("스택이 비어있습니다")
        return self.data[-1]

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

class Queue:
    def __init__(self):
        self.newest = Stack()
        self.oldest = Stack()

    def size(self):
        return self.newest.size() + self.oldest.size()

    def add(self, value):
        self.newest.push(value)

    def shift_stacks(self):
        if self.oldest.is_empty():
            while not self.newest.is_empty():
                self.oldest.push(self.newest.pop())

    def peek(self):
        self.shift_stacks()
        return self.oldest.peek()

    def remove(self):
        self.shift_stacks()
        return self.oldest.pop()

q = Queue()
q.add(1)
q.add(2)
q.add(3)
print(q.remove())
print(q.remove())
print(q.remove())