n = int(input())
prime = list(range(2, n + 1))
for i in prime:
    for j in range(i * 2, n + 1, i):
        if j in prime and j % i == 0:
            prime.remove(j)

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