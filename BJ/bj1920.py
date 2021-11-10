def merge_sort(array):
    n = len(array)
    if len(array) <= 1:
        return
    mid = n // 2
    g1 = array[:mid]
    g2 = array[mid:]
    merge_sort(g1)
    merge_sort(g2)

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) or i2 < len(g2):
        if i2 >= len(g2) or (i1 < len(g1) and g1[i1] <g2[i2]):
            array[ia] = g1[i1]
            i1 += 1
        else:
            array[ia] = g2[i2]
            i2 += 1
        ia += 1

def binary_search(array, start, end, target):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] > target:
        return binary_search(array, start, mid - 1, target)
    elif array[mid] < target:
        return binary_search(array, mid + 1, end, target)
    else:
        return 1

n = int(input())
arr = list(map(int, input().split()))
merge_sort(arr)

m = int(input())
for x in map(int, input().split()):
    print(binary_search(arr, 0, n - 1, x))