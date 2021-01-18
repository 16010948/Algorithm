def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]
    left = []
    right = []
    for x in tail:
        if x + pivot > pivot + x:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)


def solution(numbers):
    answer = ''
    numbers_to_string = list(map(str, numbers))
    sort_number = quick_sort(numbers_to_string)
    answer = ''.join(sort_number)
    if answer.startswith('0'):
        answer = "0"
    return answer

numbers = [6, 10, 2]
# answer = "6210"
print(solution(numbers))
numbers = [3, 30, 34, 5, 9]
# answer = "9534330"
print(solution(numbers))