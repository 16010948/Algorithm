def get_numbers(n, numbers):
    while n > 0:
        numbers.add(n % 10)
        n //= 10

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    numbers = set()
    i = 1
    while True:
        get_numbers(i * n, numbers)
        if len(numbers) == 10:
            break
        i += 1
    print("#" + str(test_case), i * n)