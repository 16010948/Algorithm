n = int(input())

i = 2
while i <= n:
    if n % i == 0:
        print(i)
        n = n // i
        i = 2
    else:
        i += 1