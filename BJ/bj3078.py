from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
names = []
max_length = 0
for _ in range(n):
    names.append(len(input()))
    max_length = max(max_length, names[-1])

queue = [deque() for _ in range(max_length + 1)]
answer = 0
for i, name in enumerate(names):
    while queue[name] and queue[name][0] < i - k:
        queue[name].popleft()
    answer += len(queue[name])
    queue[name].append(i)
print(answer)