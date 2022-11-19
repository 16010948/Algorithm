MAX_VALUE = 100_000

n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_length = 0
count = [0 for _ in range(MAX_VALUE + 1)]
length = 0
for i in range(n):
    if count[arr[i]] == k:
        for j in range(i - length, i):
            count[arr[j]] -= 1
            length -= 1
            if arr[j] == arr[i]:
                break
    count[arr[i]] += 1
    length += 1

    max_length = max(length, max_length)

print(max_length)