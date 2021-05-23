def factorial(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s

def solution(n, k):
    answer = []

    num = list(range(1, n + 1))
    for i in range(n - 1, -1, -1):
        f = factorial(i)
        index = k // f
        k = k % f
        if k == 0:
            index -= 1
        answer.append(num.pop(index))
    return answer

n = 3
k = 5
# answer = [3, 2, 1]
print(solution(n, k))