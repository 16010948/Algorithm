a, b, n = map(int, input().split())
division = a % b
for i in range(n - 1):
    division *= 10
    division %= b
print((division * 10) // b)