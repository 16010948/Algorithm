def convert_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    binary = convert_binary(m)
    if len(binary) < n:
        binary = "0" * (n - len(binary)) + binary
    result = "ON"
    for i in range(len(binary) - n, len(binary)):
        if binary[i] != '1':
            result ="OFF"
            break
    print("#"+str(test_case), result)