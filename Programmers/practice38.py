def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for k in range(len(arr1)):
        for i in range(len(arr2[0])):
            element = 0
            for j in range(len(arr2)):
                element += arr1[k][j] * arr2[j][i]
            answer[k][i] = element
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
# answer = [[15, 15], [15, 15], [15, 15]]
print(solution(arr1, arr2))

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
# answer = [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
print(solution(arr1, arr2))