def binomical(n, k):
    if k == 0 or n == k:
        return 1
    return binomical(n - 1, k) + binomical(n - 1, k - 1)

n, k = map(int, input().split())
print(binomical(n, k))

