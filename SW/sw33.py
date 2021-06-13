def is_increasing_number(n):
    string_number = str(n)
    for i in range(len(string_number) - 1):
        if string_number[i] > string_number[i + 1]:
            return False
    return True


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    array = list(map(int, input().split()))
    max_value = -1
    for i in range(n):
        for j in range(i + 1, n):
            multiply = array[i] * array[j]
            if max_value < multiply and is_increasing_number(multiply):
                max_value = multiply
    print("#" + str(test_case), max_value)