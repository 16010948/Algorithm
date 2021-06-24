def merge(array, l, m, r):
    i1 = l
    i2 = m + 1
    ia = l
    result = [0] * (r + 1)
    while i1 <= m and i2 <= r:
        if array[i1] < array[i2]:
            result[ia] = array[i1]
            i1 += 1
        else:
            result[ia] = array[i2]
            i2 += 1
        ia += 1

    for i in range(i1, m + 1):
        result[ia] = array[i]
        ia += 1

    for i in range(i2, r + 1):
        result[ia] = array[i]
        ia += 1

    for i in range(l, r + 1):
        array[i] = result[i]

def mg_partition(array, l, r):
    if l < r:
        m = (l + r) // 2
        mg_partition(array, l, m)
        mg_partition(array, m + 1, r)
        merge(array, l, m, r)

def merge_sort(n, array):
    mg_partition(array, 0, n - 1)
    print(array)

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    l = start + 1
    r = end
    while l <= r:
        while l <= end and array[pivot] >= array[l]:
            l += 1
        while r > start and array[pivot] <= array[r]:
            r -= 1
        if l > r:
            array[pivot], array[r] = array[r], array[pivot]
        else:
            array[l], array[r] = array[r], array[l]
    quick_sort(array, start, r - 1)
    quick_sort(array, r + 1, end)

n = int(input())
array = list(map(int, input().split()))
#merge_sort(n, array)
quick_sort(array, 0, n - 1)
print(array)