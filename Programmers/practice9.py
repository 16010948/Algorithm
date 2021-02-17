def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[pivot] >= arr[left]:
            left += 1
        while right > start and arr[pivot] <= arr[right]:
            right -= 1
        if left >= right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


def solution(A, B):
    answer = 0
    # quick_sort(A, 0, len(A) - 1)
    # quick_sort(B, 0, len(B) - 1)
    A.sort()
    B.sort()
    a_index = 0
    b_index = len(B) - 1

    while a_index <= len(A) - 1 and b_index >= 0:
        answer += A[a_index] * B[b_index]
        a_index += 1
        b_index -= 1

    return answer

A = [1, 4, 2]
B = [5, 4, 4]
# answer = 29
print(solution(A, B))

A = [1,2]
B = [3,4]
# answer = 10
print(solution(A, B))