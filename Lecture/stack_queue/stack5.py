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

class Stack_with_Min:
    def __init__(self):
        self.data = Stack()
        self.min_data = Stack()

    def min(self):
        if self.min_data.is_empty():
            return int(1e9)
        else:
            return self.min_data.peek()

    def push(self, value):
        if value < self.min():
            self.min_data.push(value)
        self.data.push(value)

    def pop(self):
        value = self.data.pop()
        if value == self.min():
            self.min_data.pop()
        return value

stack = Stack_with_Min()
stack.push(3)
stack.push(5)
stack.push(1)
stack.push(2)
print("min:", stack.min())
print("pop:", stack.pop())
print("min:", stack.min())
print("pop:", stack.pop())
print("min:", stack.min())
print("pop:", stack.pop())
print("min:", stack.min())
