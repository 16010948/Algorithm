def get_gcd(num1, num2):
    if num2 <= 0:
        return num1
    return get_gcd(num2, num1 % num2)

num1, num2 = map(int, input().split())
gcd = get_gcd(num1, num2)
print(gcd)
print(gcd * (num1  // gcd) * (num2 // gcd))
