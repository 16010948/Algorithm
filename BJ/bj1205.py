import sys
input = sys.stdin.readline

n, new_score, p = map(int, input().split())
scores = list(map(int, input().split()))

if n == p and new_score <= scores[-1]:
    print(-1)
else:
    result = 0
    for i in range(n):
        if scores[i] <= new_score:
            break
        result += 1
    print(result + 1)