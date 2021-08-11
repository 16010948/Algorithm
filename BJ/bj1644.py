n = int(input())
is_prime = [True] * (n + 1)
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * 2, n + 1, i):
            if is_prime[j] and j % i == 0:
                is_prime[j] = False

prime = [i for i in range(2, n + 1) if is_prime[i]]
end = 0
count = 0
interval_sum = 0
for start in range(len(prime)):
    while interval_sum < n and end < len(prime):
        interval_sum += prime[end]
        end += 1
    if interval_sum == n:
       count += 1
    interval_sum -= prime[start]

print(count)