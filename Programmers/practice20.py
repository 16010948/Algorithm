def solution(arr):
    answer = [arr[0]]

    for i in range(1, len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer

arr = [1, 1, 3, 3, 0, 1, 1]
# answer = [1, 3, 0, 1]
print(solution(arr))

arr = [4, 4, 4, 3, 3]
# answer = [4, 3]
print(solution(arr))