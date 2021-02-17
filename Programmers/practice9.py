def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer

A = [1, 4, 2]
B = [5, 4, 4]
# answer = 29
print(solution(A, B))

A = [1,2]
B = [3,4]
# answer = 10
print(solution(A, B))