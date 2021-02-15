def solution(n):
    answer = []

    while n > 0:
        answer.append(n % 10)
        n //= 10

    return answer

n = 12345
# answer = [5,4,3,2,1]
print(solution(n))