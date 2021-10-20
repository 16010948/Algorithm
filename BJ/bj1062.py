import sys
input = sys.stdin.readline

ANTA_TICA = {'a', 'c', 't', 'i', 'n'}
ANTA_TICA_SIZE = len({'a', 'c', 't', 'i', 'n'})
ALPHA = ord('z') - ord('a') + 1

def dfs(idx, cnt):
    global answer, learn
    if k == cnt:
        total = 0
        for word in words:
            if (word & learn) == word:
                total += 1
        answer = max(answer, total)
        return
    for i in range(idx, ALPHA):
        learn |= (1 << i)
        dfs(i + 1, cnt + 1)
        learn &= ~(1 << i)

n, k = map(int, input().split())
answer = 0

words = []
count = 0
for _ in range(n):
    word = list(set(input().strip()) - ANTA_TICA)
    value = 0
    for char in word:
        value |= (1 << (ord(char) - ord('a')))
    words.append(value)
    count += len(word)

if k < ANTA_TICA_SIZE:
    print(answer)
elif count < k -ANTA_TICA_SIZE:
    print(n)
else:
    k -= ANTA_TICA_SIZE

    learn = 0
    answer = 0
    dfs(0, 0)
    print(answer)