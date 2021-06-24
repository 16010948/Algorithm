n = int(input())

score = [n] * (n + 1)
min_score = n
while True:
    candidate1, candidate2 = map(int, input().split())
    if candidate1 < 0 and candidate2 < 0:
        break

    score[candidate1] -= 1
    score[candidate2] -= 1
    min_score = min(min_score, score[candidate1], score[candidate2])


answer = []
for i in range(1, n + 1):
    if score[i] == min_score:
        answer.append(i)

print(min_score, len(answer))
print(' '.join(str(item) for item in answer))