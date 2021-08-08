class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

n = int(input())
expression = list(input())

values = {}
for i in range(n):
    values[chr(ord('A') + i)] = int(input())

stack = Stack()
for token in expression:
    if token.isalpha():
        stack.push(values[token])
    else:
        b = stack.pop()
        a = stack.pop()
        if token == '+':
            stack.push(a + b)
        elif token == '-':
            stack.push(a - b)
        elif token == '*':
            stack.push(a * b)
        elif token == '/':
            stack.push(a / b)
print("{:.2f}".format(stack.pop()))