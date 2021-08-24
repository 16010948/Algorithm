n = int(input())
files = map(int, input().split())
cluster = int(input())

total = 0
for file in files:
    size = file // cluster
    if file % cluster != 0:
        size += 1
    total += cluster * size
print(total)