def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while right > start and array[pivot] <= array[right]:
            right -= 1
        if left >= right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

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
quick_sort(arr, 0, n - 1)
m = int(input())
for x in map(int, input().split()):
    print(binary_search(arr, 0, n - 1, x))