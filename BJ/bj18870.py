def binary_search(target, array):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

n = int(input())
coordinates = list(map(int, input().split()))
non_duplicate_coordinates = list(set(coordinates))

non_duplicate_coordinates.sort()
for coordinate in coordinates:
    print(binary_search(coordinate, non_duplicate_coordinates), end=" ")