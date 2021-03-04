def binary_search(array, start, end, target):
    if start > end:
        return start
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, start, mid - 1, target)
    else:
        return binary_search(array, mid + 1, end, target)


def solution(s):
    answer = ''

    lower = []
    bigger = []
    for c in s:
        if c.islower():
            lower_index = binary_search(lower, 0, len(lower) - 1, c)
            lower.insert(lower_index, c)
        else:
            bigger_index = binary_search(bigger, 0, len(bigger) - 1, c)
            bigger.insert(bigger_index, c)
    answer = ''.join(lower) + ''.join(bigger)
    return answer

s = "Zbcdefg"
# answer = "gfedcbZ"
print(solution(s))