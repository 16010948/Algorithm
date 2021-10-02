n, m = map(int, input().split())

values = [0] + list(map(int, input().split()))

arr = [0] * (n + 2)
for _ in range(m):
    start, end, k = map(int, input().split())
    arr[start] += k
    arr[end + 1] -= k

for i in range(1, n + 1):
    arr[i] = arr[i - 1] + arr[i]

for i in range(1, n + 1):
    print(arr[i] + values[i], end= " ")