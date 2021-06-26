def convert_369(n):
    result = ''

    origin = n
    while n > 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            result += '-'
        n //= 10

    if len(result) == 0:
        result = origin

    return result


n = int(input())

for i in range(1, n + 1):
    print(convert_369(i), end=" ")