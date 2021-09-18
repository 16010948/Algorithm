n, k = map(int, input().split())

jewelry = []
for _ in range(n):
    jewelry.append(tuple(map(int, input().split())))

bag = []
for _ in range(k):
    bag.append(int(input()))

for i in range(len(bag)):
    dp = [0] * (bag[i] + 1)
    for j in range(len(jewelry)):
        if bag[i] >= jewelry[j][0]:
            total += jewelry[j][1]
            del jewelry[j]
            break

print(total)