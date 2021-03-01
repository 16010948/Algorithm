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
        if g1[i1] > g2[i2]:
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

for _ in range(n):
    m, printer = map(int, input().split())
    priorities = list(map(int, input().split()))
    queue = []
    for i in range(m):
        queue.append((i, priorities[i]))
    merge_sort(priorities)
    count = 0
    index = 0
    while True:
        value = queue.pop(0)
        if value[1] == priorities[index]:
            index = (index + 1) % m
            count += 1
            if value[0] == printer:
                break
        else:
            queue.append(value)
    print(count)