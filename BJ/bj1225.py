a, b = map(int, input().split())

sum_a = 0
while a > 0:
    sum_a += a % 10
    a //= 10

sum_b = 0
while b > 0:
    sum_b += b % 10
    b //= 10
print(sum_a * sum_b)