import sys
input = sys.stdin.readline
class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.empty():
            return -1
        return self.data.pop()

    def size(self):
        return len(self.data)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def top(self):
        if self.empty():
            return -1
        return self.data[-1]

n = int(input())

stack = Stack()
for _ in range(n):
    op = input().split()
    if op[0] == 'push':
        stack.push(int(op[1]))
    elif op[0] == 'pop':
        print(stack.pop())
    elif op[0] == 'size':
        print(stack.size())
    elif op[0] == 'empty':
        print(stack.empty())
    elif op[0] == 'top':
        print(stack.top())