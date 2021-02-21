import sys
from collections import deque
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.data = deque([])

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.size() == 0:
            return -1
        return self.data.popleft()

    def size(self):
        return len(self.data)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def front(self):
        if self.size() == 0:
            return -1
        return self.data[0]

    def back(self):
        if self.size() == 0:
            return -1
        return self.data[-1]

n = int(input())
q = Queue()
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        q.push(int(command[1]))
    elif command[0] == "pop":
        print(q.pop())
    elif command[0] == "size":
        print(q.size())
    elif command[0] == "empty":
        print(q.empty())
    elif command[0] == "front":
        print(q.front())
    elif command[0] == "back":
        print(q.back())