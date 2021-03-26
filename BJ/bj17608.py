import sys
input = sys.stdin.readline

n = int(input())
bars = []
for _ in range(n):
    bar = int(input())

    while bars and bars[-1] <= bar:
        bars.pop()

    bars.append(bar)
print(len(bars))