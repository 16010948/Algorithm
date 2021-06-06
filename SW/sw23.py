INF = int(1e9)


def find_max(array):
    max_value = 0
    for num in array:
        if num > max_value:
            max_value = num

    return max_value


def find_min(array):
    min_value = INF
    for num in array:
        if num < min_value:
            min_value = num

    return min_value


def find_normal_count(array):
    count = 0
    for i in range(1, len(array) - 1):
        min_value = find_min([array[i - 1], array[i], array[i + 1]])
        max_value = find_max([array[i - 1], array[i], array[i + 1]])
        if array[i] not in (min_value, max_value):
            count += 1

    return count


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    array = list(map(int, input().split()))

    count = find_normal_count(array)
    print("#" + str(test_case), count)
