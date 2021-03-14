def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i].append(arr1[i][j] + arr2[i][j])

    return answer

arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]
# answer = [[4,6],[7,9]]
print(solution(arr1, arr2))

arr1 = [[1], [2]]
arr2 = [[3], [4]]
# answer = [[4],[6]]
print(solution(arr1, arr2))