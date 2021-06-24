def sort_by_weight(array):
    n = len(array)
    if n <= 1:
        return array
    mid = n // 2
    g1 = array[:mid]
    g2 = array[mid:]
    sort_by_weight(g1)
    sort_by_weight(g2)

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1][1] > g2[i2][1]:
            array[ia] = g1[i1]
            i1 += 1
        elif g1[i1][1] == g2[i2][1]:
            if g1[i1][0] > g2[i2][0]:
                array[ia] = g1[i1]
                i1 += 1
            else:
                array[ia] = g2[i2]
                i2 += 1
        else:
            array[ia] = g2[i2]
            i2 += 1
        ia += 1

    for i in range(i1, len(g1)):
        array[ia] = g1[i]
        ia += 1

    for i in range(i2, len(g2)):
        array[ia] = g2[i]
        ia += 1

def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array
    mid = n // 2
    g1 = array[:mid]
    g2 = array[mid:]
    sort_by_weight(g1)
    sort_by_weight(g2)

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            array[ia] = g1[i1]
            i1 += 1
        else:
            array[ia] = g2[i2]
            i2 += 1
        ia += 1

    for i in range(i1, len(g1)):
        array[ia] = g1[i]
        ia += 1

    for i in range(i2, len(g2)):
        array[ia] = g2[i]
        ia += 1

n, k = map(int, input().split())

jewelry = []
for _ in range(n):
    jewelry.append(tuple(map(int, input().split())))

bag = []
for _ in range(k):
    bag.append(int(input()))

sort_by_weight(jewelry)
merge_sort(bag)

total = 0
for i in range(len(bag)):
    for j in range(len(jewelry)):
        if bag[i] >= jewelry[j][0]:
            total += jewelry[j][1]
            del jewelry[j]
            break

print(total)