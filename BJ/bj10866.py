import sys
from collections import deque
input = sys.stdin.readline

class Deque:
    def __init__(self):
        self.data = deque([])

    def push_front(self, x):
        self.data.insert(0, x)

    def push_back(self, x):
        self.data.append(x)

    def pop_front(self):
        if self.size() == 0:
            return -1
        return self.data.popleft()

    def pop_back(self):
        if self.size() == 0:
            return -1
        return self.data.pop()

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
q = Deque()
for _ in range(n):
    command = input().split()
    if command[0] == "push_front":
        q.push_front(int(command[1]))
    elif command[0] == "push_back":
        q.push_back(int(command[1]))
    elif command[0] == "pop_front":
        print(q.pop_front())
    elif command[0] == "pop_back":
        print(q.pop_back())
    elif command[0] == "size":
        print(q.size())
    elif command[0] == "empty":
        print(q.empty())
    elif command[0] == "front":
        print(q.front())
    elif command[0] == "back":
        print(q.back())