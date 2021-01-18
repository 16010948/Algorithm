a, b, v = map(int, input().split())

count = ((v - a) / (a - b)) + 1

if count - int(count) > 0:
    print(int(count) + 1)
else:
    print(int(count))