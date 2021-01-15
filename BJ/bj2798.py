N, M = map(int, input().split())
cards = list(map(int, input().split()))
minGap = 100000
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            cardSum = cards[i] + cards[j] + cards[k]
            gap = M - cardSum
            if 0 <= gap and gap < minGap:
                minGap = gap
                result = cardSum
print(result)