def solution(n):
    answer = (int(n ** 0.5) + 1) ** 2 if int(n ** 0.5) ** 2 == n else -1
    return answer

n = 121
# answer = 144
print(solution(n))

n = 3
# answer = -1
print(solution(n))