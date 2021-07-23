from collections import deque
n, l = map(int, input().split())
array = list(map(int, input().split()))

queue = deque()
for i in range(n):
    while queue and queue[-1][0] > array[i]:
        queue.pop()
    queue.append((array[i], i))
    if queue[0][1] <= i - l:
        queue.popleft()

    print(queue[0][0], end=" ")