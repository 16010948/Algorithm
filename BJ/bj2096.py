import sys
input = sys.stdin.readline

n = int(input())

min_scores = []
max_scores = []
deltas = [-1, 0, 1]
for y in range(n):
    scores = list(map(int, input().split()))
    if y == 0:
        min_scores.append(scores)
        max_scores.append(scores)
    else:
        min_scores.append([int(1e9)] * 3)
        max_scores.append([0] * 3)
        for x in range(3):
            for delta in deltas:
                nx = x + delta
                if 0 <= nx and nx < 3:
                    max_scores[1][x] = max(max_scores[1][x], max_scores[0][nx] + scores[x])
                    min_scores[1][x] = min(min_scores[1][x], min_scores[0][nx] + scores[x])
        max_scores = [max_scores[1]]
        min_scores = [min_scores[1]]

print(max(max_scores[-1]), min(min_scores[-1]))