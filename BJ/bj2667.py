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

def get_area(complex, i, j, visited, area):
    if not visited[i][j] and complex[i][j] == 1:
        visited[i][j] = True
        area += 1
        if i > 0:
            area = get_area(complex, i - 1, j, visited, area)
        if i < n - 1:
            area = get_area(complex, i + 1, j, visited, area)
        if j > 0:
            area = get_area(complex, i, j - 1, visited, area)
        if j < n - 1:
            area = get_area(complex, i, j + 1, visited, area)
    return area

n = int(input())

complex = []
for _ in range(n):
    complex.append(list(map(int, list(input()))))

visited = [[False] * n for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        area = get_area(complex, i, j, visited, 0)
        if area != 0:
            result.append(area)
merge_sort(result)

print(len(result))
for r in result:
    print(r)