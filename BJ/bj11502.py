def make_prime_sum(odd, s, cnt):
    if cnt == 3:
        if odd == sum(s):
            return s
        return None

    for prime in primes:
        if prime <= odd - sum(s):
            result = make_prime_sum(odd, s + [prime], cnt + 1)
            if result:
                return result


MAX = 1000

is_prime = [True] * (MAX + 1)
for i in range(2, int(MAX ** 0.5) + 1):
    for j in range(i * i, MAX + 1, i):
        is_prime[j] = False

primes = []
for i in range(2, MAX + 1):
    if is_prime[i]:
        primes.append(i)


n = int(input())
for _ in range(n):
    odd = int(input())
    nums = make_prime_sum(odd, [], 0)

    if nums:
        print(' '.join([str(num) for num in nums]))
    else:
        print(0)