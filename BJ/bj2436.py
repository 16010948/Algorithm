def get_gcd(num1, num2):
    if num2 == 0:
        return num1
    return get_gcd(num2, num1 % num2)

def get_factor(n, gcd):
    min_factor = []
    for i in range(1, int(n ** 0.5) + 1):
        if get_gcd(gcd * n // i, gcd * i) == gcd and n % i == 0:
            min_factor = [i, n // i]
    return min_factor

gcd, lcm = map(int, input().split())

min_factor = get_factor(lcm // gcd, gcd)

print(gcd * min_factor[0], gcd * min_factor[1])