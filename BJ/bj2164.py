from collections import deque

class Queue:
    def __init__(self, n):
        self.data = deque(list(range(1, n + 1)))

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
card = Queue(n)

while card.size() > 1:
    card.pop()
    card.push(card.pop())
print(card.front())
