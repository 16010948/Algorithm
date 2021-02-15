def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[pivot] <= arr[left]:
            left += 1
        while right > start and arr[pivot] >= arr[right]:
            right -= 1
        if left >= right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


def solution(n):
    answer = 0
    arr = []
    while n > 0:
        arr.append(str(n % 10))
        n //= 10
    quick_sort(arr, 0, len(arr) - 1)
    answer = int(''.join(arr))
    return answer

n = 118372
# answer = 873211
print(solution(n))