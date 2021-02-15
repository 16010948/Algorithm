def solution(n, m):
    answer = []
    gcm = 1
    i = 2
    a = n
    b = m
    while a >= i and b >= i:
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i
            gcm *= i
        else:
            i += 1
    lcm = gcm * (n // gcm) * (m // gcm)
    answer = [gcm, lcm]
    return answer

n = 3
m = 12
# answer = [3, 12]
print(solution(n, m))

n = 2
m = 5
# answer = [1, 10]
print(solution(n, m))