def solution(n):
    answer = 0

    while n > 0:
        answer += n % 10
        n //= 10

    return answer

n = 123
# answer = 6
print(solution(n))

n = 987
# answer = 24
print(solution(n))