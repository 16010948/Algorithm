def heapify(array, n, i):
    p = i
    l = i * 2 + 1
    r = i * 2 + 2

    if l < n and array[p] < array[l]:
        p = l

    if r < n and array[p] < array[r]:
        p = r

    if i != p:
        swap(array, p, i)
        heapify(array, n, p)

def swap(array, a, b):
    array[a], array[b] = array[b], array[a]

def heap_sort(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, -1, -1):
        swap(array, 0, i)
        heapify(array, i, 0)

array = [230, 10, 60, 550, 40, 220, 20]

heap_sort(array)

for item in array:
    print(item)