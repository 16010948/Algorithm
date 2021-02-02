import sys
n = int(sys.stdin.readline())

counting = [0] * (10000 + 1)

for _ in range(n):
    counting[int(sys.stdin.readline())] += 1
count = 0
for i in range(1, 10000 + 1):
    for _ in range(counting[i]):
        print(i)
    count += counting[i]
    if count == n:
        break