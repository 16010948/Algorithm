def fibonacci(n):
    fib1 = 0
    fib2 = 1

    for i in range(2, n + 1):
        fib = (fib1 + fib2) % 1234567
        fib1 = fib2
        fib2 = fib
    return fib


def solution(n):
    answer = fibonacci(n)
    return answer

n = 3
# answer = 2
print(solution(n))

n = 5
# answer = 5
print(solution(n))