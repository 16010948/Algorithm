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


def solution(s):
    answer = ''

    numbers = list(map(int, s.split()))
    quick_sort(numbers, 0, len(numbers) - 1)
    answer = str(numbers[0]) + " " + str(numbers[-1])

    return answer

s = "1 2 3 4"
# answer = "1 4"
print(solution(s))

s = "-1 -2 -3 -4"
# answer = "-4 -1"
print(solution(s))

s = "-1 -1"
# answer = "-1 -1"
print(solution(s))