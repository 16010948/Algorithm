def long_run(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    a = 1
    b = 2
    s = 0
    for i in range(3, n + 1):
        s = (a + b) % 1234567
        a = b
        b = s
    return s


def solution(n):
    answer = long_run(n)
    return answer

n = 4
# answer = 5
print(solution(n))

n = 3
# answer = 3
print(solution(n))