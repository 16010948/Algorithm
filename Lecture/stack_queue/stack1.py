class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None
    def pop(self):
        if self.top == None:
            raise Exception("스택이 비어있습니다")
        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, item):
        node = self.Node(item)
        node.next = self.top
        self.top = node

    def peek(self):
        if self.top == None:
            raise Exception("스택이 비어있습니다")
        return self.top.data

    def is_empty(self):
        return self.top == None

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.pop())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.is_empty())
print(s.pop())
print(s.is_empty())