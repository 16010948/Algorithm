n, s = map(int, input().split())
array = list(map(int, input().split()))


interval_sum = 0
end = 0
answer = 0
for start in range(n):
    while end < n and interval_sum < s:
        interval_sum += array[end]
        end += 1
    if interval_sum == s:
        answer += 1
    interval_sum -= array[start]
print(answer)