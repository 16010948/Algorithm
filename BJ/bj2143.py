def bisect_left(array, target):
    start = 0
    end = len(array)
    while start < end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end

def bisect_right(array, target):
    start = 0
    end = len(array)
    while start < end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid
        else:
            start = mid + 1
    return end

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
    while i1 < len(g1) or i2 < len(g2):
        if i2 >= len(g2) or (i1 < len(g1) and g1[i1] < g2[i2]) :
            array[ia] = g1[i1]
            i1 += 1
        else:
            array[ia] = g2[i2]
            i2 += 1
        ia += 1

t = int(input())

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a_sum = []
for i in range(n):
    a_sum.append(a[i])
    interval_sum = a[i]
    for j in range(i + 1, n):
        interval_sum += a[j]
        a_sum.append(interval_sum)

b_sum = []
for i in range(m):
    b_sum.append(b[i])
    interval_sum = b[i]
    for j in range(i + 1, m):
        interval_sum += b[j]
        b_sum.append(interval_sum)
merge_sort(b_sum)

answer = 0
for a_interval in a_sum:
    start_idx = bisect_left(b_sum, t - a_interval)
    end_idx = bisect_right(b_sum, t - a_interval)
    answer += end_idx - start_idx
print(answer)