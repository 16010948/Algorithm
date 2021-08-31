min_value, max_value = map(int, input().split())

is_pow = [False] * (max_value - min_value + 1)
count = max_value - min_value + 1
for i in range(2, int(max_value ** 0.5) + 1):
    square = i * i
    j = min_value // square
    while square * j <= max_value:
        index = ((square * j) - min_value)
        if index >= 0 and not is_pow[index]:
            count -= 1
            is_pow[index] = True
        j += 1
print(count)