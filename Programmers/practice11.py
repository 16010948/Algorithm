def solution(n):
    answer = n - 1
    prime = [True] * (n + 1)
    for i in range(2, int(n ** (1 / 2)) + 1):
        if prime[i] == True:
            for j in range(i * i, n + 1, i):
                if j % i == 0 and prime[j]:
                    prime[j] = False
                    answer -= 1

    return answer

n = 10
# answer = 4
print(solution(n))

n = 5
# answer = 3
print(solution(n))