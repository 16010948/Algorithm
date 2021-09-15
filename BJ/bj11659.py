import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = [0] + list(map(int, input().split()))
interval = [0]
for i in range(1, n + 1):
    interval.append(interval[-1] + array[i])

for _ in range(m):
    start, end = map(int, input().split())
    print(interval[end] - interval[start - 1])
