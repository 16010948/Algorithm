def solution(n):
    answer = 0

    ternary = []
    while n > 0:
        ternary.append(n % 3)
        n //= 3

    for i, bit in enumerate(ternary):
        answer += bit * (3 ** (len(ternary) - i - 1))

    return answer

n = 45
# answer = 7
print(solution(n))

n = 125
# answer = 229
print(solution(n))