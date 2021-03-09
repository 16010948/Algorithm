n = int(input())

factorial = 1
for i in range(2, n + 1):
    factorial *= i

count = 0
while factorial > 0:
    if factorial % 10 == 0:
        count += 1
    else:
        break
    factorial //= 10

print(count)