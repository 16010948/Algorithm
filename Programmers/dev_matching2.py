def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def solution(lottos, win_nums):
    answer = []
    LOTTO = 6

    quick_sort(win_nums, 0, LOTTO - 1)
    blurry = 0
    correct = 0
    visited = [False] * LOTTO
    for i in range(LOTTO):
        if lottos[i] == 0:
            blurry += 1
            continue
        if binary_search(win_nums, lottos[i]) >= 0:
            correct += 1

    answer = [min(LOTTO, LOTTO - (correct + blurry) + 1), min(LOTTO, LOTTO - correct + 1)]
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
# answer = [3, 5]
print(solution(lottos, win_nums))

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
# answer = [1, 6]
print(solution(lottos, win_nums))

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
# answer = [1, 1]
print(solution(lottos, win_nums))