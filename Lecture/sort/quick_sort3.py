def quick_sort(arr, start, end):
    part = partition(arr, start, end)
    if start < part - 1:
        quick_sort(arr, start, part - 1)
    if part < end:
        quick_sort(arr, part, end)

def partition(arr, start, end):
    pivot = arr[(start + end) // 2]
    while start <= end:
        while pivot > arr[start]:
            start += 1
        while pivot < arr[end]:
            end -= 1
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    return start

def print_arr(arr):
    for data in arr:
        print(data, end=", ")
    print()

array = [3, 9, 4, 7, 5, 0, 1, 6, 8, 2]
print_arr(array)
quick_sort(array, 0, len(array) - 1)
print_arr(array)