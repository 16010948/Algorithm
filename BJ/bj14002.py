n = int(input())
array = list(map(int, input().split()))


dp = [1] * n
max_length = 1
for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[j] + 1, dp[i])
            max_length = max(dp[i], max_length)

print(max_length)
stack = []
cur_length = max_length
for i in range(n - 1, -1, -1):
    if dp[i] == cur_length:
        stack.append(array[i])
        cur_length -= 1

for i in range(max_length - 1, -1, -1):
    print(stack[i], end=" ")