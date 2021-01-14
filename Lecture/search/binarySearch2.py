def bisect_left(array, start, end, target):
    while start < end:
        mid = (start + end) // 2
        if target <= array[mid]:
            end = mid
        else:
            start = mid + 1
    return end

def bisect_right(array, start, end, target):
    while start < end:
        mid = (start + end) // 2
        if target >= array[mid]:
            start = mid + 1
        else:
            end = mid
    return start

def count_by_range(array, N, x):
    left_index = bisect_left(array, 0, N - 1, x)
    right_index = bisect_right(array, 0, N - 1, x)
    print(left_index, right_index)
    return right_index - left_index

# 정렬된 배열에서 특정 수의 개수 구하기
N, x = map(int, input().split())
array = list(map(int, input().split()))
print(count_by_range(array, N, x))