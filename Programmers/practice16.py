def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if n % i == 0:
            answer += i

    return answer

n = 12
# answer = 28
print(solution(n))

n = 5
# answer = 6
print(solution(n))