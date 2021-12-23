def parse_decimal(binary):
    decimal = 0
    base = 1

    for i in range(len(binary) - 1, -1, -1):
        decimal += int(binary[i]) * base
        base *= 2
    return decimal

def parse_binary(result):
    answer = ''
    while result > 0:
        answer = str(result % 2) + answer
        result //= 2

    if not answer:
        answer = '0'

    return answer

tc = int(input())

for _ in range(tc):
    binary1, binary2 = input().split()
    decimal1 = parse_decimal(binary1)
    decimal2 = parse_decimal(binary2)
    result = decimal1 + decimal2
    answer = parse_binary(result)
    print(answer)