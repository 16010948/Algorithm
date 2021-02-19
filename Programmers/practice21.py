def string_nth_index_sort(array, start, end, n):
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and (
                array[pivot][n] > array[left][n] or (array[pivot][n] == array[left][n] and array[pivot] > array[left])):
            left += 1
        while right > start and (array[pivot][n] < array[right][n] or (
                array[pivot][n] == array[right][n] and array[pivot] < array[right])):
            right -= 1
        if left >= right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    string_nth_index_sort(array, start, right - 1, n)
    string_nth_index_sort(array, right + 1, end, n)


def solution(strings, n):
    answer = []

    string_nth_index_sort(strings, 0, len(strings) - 1, n)

    answer = strings

    return answer

strings = ["sun", "bed", "car"]
n = 1
# answer = 	["car", "bed", "sun"]
print(solution(strings, n))

strings = ["abce", "abcd", "cdx"]
n = 2
# answer = 	["abcd", "abce", "cdx"]
print(solution(strings, n))