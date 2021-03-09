t = int(input())

for i in range(t):
    n = int(input())

    if n == 0:
        print(n)
        continue

    fashion = {}
    total = 1
    for j in range(n):
        cloth, category = input().split()
        if category in fashion.keys():
            fashion[category] += 1
        else:
            fashion[category] = 1
    for category in fashion.keys():
        total *= fashion[category] + 1

    print(total - 1)