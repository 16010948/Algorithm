num = list(map(int, list(input())))

result = num[0]
for i in range(1, len(num)):
    if num[i] <= 1 or result <= 1:
        result += num[i]
    else:
        result *= num[i]
print(result)