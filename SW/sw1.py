import re

LID_SIZE = 4
HEXA = 16


def parse_decimal(hexadecimal, size):
    hexa_base = 1
    decimal = 0
    for i in range(size - 1, -1, -1):
        if hexadecimal[i].isalpha():
            num = ord(hexadecimal[i]) - ord('A') + 10
        else:
            num = int(hexadecimal[i])
        decimal += num * hexa_base
        hexa_base *= HEXA
    return decimal


def merge_sort(array):
    n = len(array)
    if n <= 1:
        return
    mid = n // 2
    g1 = array[:mid]
    g2 = array[mid:]
    merge_sort(g1)
    merge_sort(g2)
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] > g2[i2]:
            array[ia] = g1[i1]
            i1 += 1
        else:
            array[ia] = g2[i2]
            i2 += 1
        ia += 1

    for i in range(i1, len(g1)):
        array[ia] = g1[i]
        ia += 1
    for i in range(i2, len(g2)):
        array[ia] = g2[i]
        ia += 1


T = int(input())

for test_case in range(1, T + 1):
    result = set()
    n, k = map(int, input().split())
    password = input()
    password_size = n // LID_SIZE
    for _ in range(password_size):
        for hexadecimal in re.findall('.{' + str(password_size) + '}', password):
            result.add(parse_decimal(hexadecimal, password_size))
        password = password[1:] + password[0]
    result = list(result)
    merge_sort(result)
    print("#" + str(test_case), result[k - 1])