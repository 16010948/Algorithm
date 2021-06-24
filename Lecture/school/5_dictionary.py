def binary_search(array, target):
    start = 0
    end = len(array) - 1
    while True:
        mid = (start + end) // 2
        if start == end:
            if array[mid] >= target:
                return mid
            else:
                return mid + 1
        if array[mid] == target:
            return n
        elif array[mid] > target:
            end = mid
        elif array[mid] < target:
            start = mid + 1

n, target = map(int, input().split())
array = list(map(int, input().split()))
print(binary_search(array, target))