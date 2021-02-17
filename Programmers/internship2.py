def length_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and len(array[pivot]) >= len(array[left]):
            left += 1
        while right > start and len(array[pivot]) <= len(array[right]):
            right -= 1
        if left >= right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    length_sort(array, start, right - 1)
    length_sort(array, right + 1, end)


def solution(s):
    answer = []
    s1 = s.lstrip('{').rstrip('}').split('},{')
    new_s = []

    for i in s1:
        new_s.append(list(map(int, i.split(','))))

    length_sort(new_s, 0, len(new_s) - 1)

    for wout_dupl_tuple in new_s:
        for item in wout_dupl_tuple:
            if item not in answer:
                answer.append(item)

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# answer = [2, 1, 3, 4]
print(solution(s))

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
# answer = [2, 1, 3, 4]
print(solution(s))

s = "{{20,111},{111}}"
# answer = [111, 20]
print(solution(s))

s = "{{123}}"
# answer = [123]
print(solution(s))

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
# answer = [3, 2, 4, 1]
print(solution(s))

