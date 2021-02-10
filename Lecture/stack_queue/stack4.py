class Node_with_Min:
    def __init__(self, v, m):
        self.value = v
        self.min = m

class Stack_with_Min:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        return self.data[-1]

    def min(self):
        if self.is_empty():
            return int(1e9)
        else:
            return self.peek().min

    def push(self, value):
        new_min = min(value, self.min())
        self.data.append(Node_with_Min(value, new_min))

    def pop(self):
        return self.data.pop()

stack = Stack_with_Min()
stack.push(3)
stack.push(5)
stack.push(1)
stack.push(2)
print("min", stack.min())
print(stack.pop().value)
print(stack.pop().value)
print("min", stack.min())