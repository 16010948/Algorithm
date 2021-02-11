def merge_sort(arr, tmp, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, tmp, start, mid)
        merge_sort(arr, tmp, mid + 1, end)
        merge(arr, tmp, start, mid, end)

def merge(arr, tmp, start, mid, end):
    for i in range(start, end + 1):
        tmp[i] = arr[i]
    part1 = start
    part2 = mid + 1
    index = start

    while part1 <= mid and part2 <= end:
        if tmp[part1] <= tmp[part2]:
            arr[index] = tmp[part1]
            part1 += 1
        else:
            arr[index] = tmp[part2]
            part2 += 1
        index += 1
    for i in range((mid - part1) + 1):
        arr[index + i] = tmp[part1 + i]

def print_array(arr):
    for data in arr:
        print(data, end=", ")
    print()

array = [3, 9, 4, 7, 5, 0, 1, 6, 8, 2]
tmp = [0] * len(array)
print_array(array)
merge_sort(array, tmp, 0, len(array) - 1)
print_array(array)