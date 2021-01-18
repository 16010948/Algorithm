def quick_sort(array, start, end):
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while right > start and array[pivot] <= array[right]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def solution(array, commands):
    answer = []

    for command in commands:
        sub_array = array[command[0] - 1:command[1]]
        quick_sort(sub_array, 0, len(sub_array) - 1)
        answer.append(sub_array[command[2] - 1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# answer = [5, 6, 3]
print(solution(array, commands))