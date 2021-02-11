n, s = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
total = 0
min_len = 100001
for start in range(n):
    while total < s and end < n:
        total += arr[end]
        end += 1
    if total >= s:
        min_len = min(min_len, end - start)
    total -= arr[start]
if min_len >= 100001:
    print(0)
else:
    print(min_len)