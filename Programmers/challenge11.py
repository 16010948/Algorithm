def convert_binary(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return '0' + binary


def make_next(binary):
    binary = list(binary)
    for i in range(len(binary) - 1, 0, -1):
        if binary[i] + binary[i - 1] == '10':
            binary[i] = '0'
            binary[i - 1] = '1'
            break
    return ''.join(binary)


def convert_decimal(n):
    decimal = 0
    two = 1
    for i in range(len(n) - 1, -1, -1):
        decimal += int(n[i]) * two
        two *= 2
    return decimal


def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            binary = convert_binary(number)
            next_binary = make_next(binary)
            decimal = convert_decimal(next_binary)
            answer.append(decimal)

    return answer

numbers = [2, 7]
# answer = [3, 11]
print(solution(numbers))
