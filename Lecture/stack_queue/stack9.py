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

def sort(s1):
    s2 = Stack()
    while not s1.is_empty():
        tmp = s1.pop()
        while not s2.is_empty() and s2.peek() > tmp:
            s1.push(s2.pop())
        s2.push(tmp)
    while not s2.is_empty():
        s1.push(s2.pop())

s1 = Stack()
s1.push(3)
s1.push(5)
s1.push(1)
s1.push(6)
sort(s1)
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())