def merge_sort(array):
    n = len(array)
    if n <= 1:
        return
    mid = n // 2
    g1 = array[:mid]
    g2 = array[mid:]
    merge_sort(g1)
    merge_sort(g2)

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


n, m = map(int, input().split())
dictionary = {}

count = 0
answer = []
for i in range(n + m):
    name = input()
    if name in dictionary:
        dictionary[name] += 1
        count += 1
        answer.append(name)
    else:
        dictionary[name] = 1

merge_sort(answer)
print(count)
for name in answer:
    print(name)