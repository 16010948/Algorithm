def solution(arr):
    answer = arr

    min_value = int(1e9)
    for i in range(len(arr)):
        if answer[i] < min_value:
            min_value = answer[i]

    answer.remove(min_value)

    if len(answer) == 0:
        answer.append(-1)

    return answer

arr = [4, 3, 2, 1]
# answer = [4, 3, 2]
print(solution(arr))

arr = [10]
# answer = [-1]
print(solution(arr))