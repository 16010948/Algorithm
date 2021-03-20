n = int(input())

a = list(map(int, input().split()))
b, c = map(int, input().split())

count = 0
for i in range(n):
    count += 1
    if a[i] > b:
        count += ((a[i] - b) // c) + (1 if (a[i] - b) % c > 0 else 0)
print(count)