class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

T = int(input())

for _ in range(T):
    sentence = input().split()
    for word in sentence:
        stack = Stack()
        for alpha in word:
            stack.push(alpha)
        while not stack.is_empty():
            print(stack.pop(), end="")
        print(end=" ")
    print(" ")