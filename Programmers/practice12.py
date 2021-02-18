def solution(n):
    answer = '수박' * n
    return answer[:n]
n = 3
# answer = "수박수"
print(solution(n))

n = 4
# answer = "수박수박"
print(solution(n))