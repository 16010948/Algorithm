def binary_search(arr, start, end, target):
    if start > end:
        return start
    mid = (start + end) // 2
    if arr[mid] > target:
        return binary_search(arr, start, mid - 1, target)
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, end, target)
    else:
        return mid + 1


def solution(arr, divisor):
    answer = []

    for item in arr:
        if item % divisor == 0:
            index = binary_search(answer, 0, len(answer) - 1, item)
            answer.insert(index, item)

    if len(answer) == 0:
        answer.append(-1)

    return answer

arr = [5, 9, 7, 10]
divisor = 5
# answer = [5, 10]
print(solution(arr, divisor))

arr = [2, 36, 1, 3]
divisor = 1
# answer = [1, 2, 3, 36]
print(solution(arr, divisor))

arr = [3, 2, 6]
divisor = 10
# answer = [-1]
print(solution(arr, divisor))