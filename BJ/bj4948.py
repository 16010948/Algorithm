while True:
    n = int(input())
    if n == 0:
        break

    prime = [True] * (2*n + 1)
    count = n
    for i in range(2, int((2 * n) ** 0.5) + 1):
        if prime[i] == True:
            for j in range(i*i, 2*n + 1, i):
                if prime[j] and j % i == 0:
                    prime[j] = False

    print(prime[2 if n < 2 else n + 1:].count(True))