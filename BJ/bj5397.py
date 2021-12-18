class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)

        self.head.next = self.tail

        self.cursor = self.tail
        self.size = 0

    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True

    def left(self):
        if self.cursor is not self.head.next:
            self.cursor = self.cursor.prev

    def right(self):
        if self.cursor is not self.tail:
            self.cursor = self.cursor.next

    def append(self, data):
        if self.is_empty():
            node = Node(data, self.head, self.tail)
            self.head.next = node
            self.tail.prev = node
        else:
            node = Node(data, self.cursor.prev, self.cursor)
            self.cursor.prev.next = node
            self.cursor.prev = node
        self.size += 1

    def pop(self):
        if not self.is_empty() and self.cursor is not self.head.next:
            popped = self.cursor.prev.data
            self.cursor.prev = self.cursor.prev.prev
            self.cursor.prev.next = self.cursor
            self.size -= 1
            return popped
        else:
            return None

    def print(self):
        cur = self.head.next
        while cur != self.tail:
            print(cur.data, end="")
            cur = cur.next


n = int(input())

for _ in range(n):
    word = input()
    password = LinkedList()
    for char in word:
        if char == '>':
            password.right()
        elif char == '<':
            password.left()
        elif char == '-':
            password.pop()
        else:
            password.append(char)
    password.print()
    print()