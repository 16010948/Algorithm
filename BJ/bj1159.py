def merge_sort(array):
    length = len(array)
    if length <= 1:
        return
    mid = length // 2
    g1 = array[:mid]
    g2 = array[mid:]
    merge_sort(g1)
    merge_sort(g2)

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if ord(g1[i1]) < ord(g2[i2]):
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

n = int(input())

player = {}
first = set()
for _ in range(n):
    name = input()
    if name[0] in player:
        player[name[0]] += 1
        if player[name[0]] >= 5:
            first.add(name[0])
    else:
        player[name[0]] = 1

if len(first) == 0:
    print("PREDAJA")
else:
    first = list(first)
    merge_sort(first)
    print(''.join(first))