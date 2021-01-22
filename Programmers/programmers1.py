def solution(n):
    answer = ''
    number = ['1', '2', '4']

    while n > 0:
        n -= 1
        answer = number[n % 3] + answer
        n //= 3
    return answer
n = 1
# answer = 1
print(solution(n))

n = 2
# answer = 2
print(solution(n))

n = 3
# answer = 4
print(solution(n))

n = 4
# answer = 11
print(solution(n))