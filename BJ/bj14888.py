max_value = int(-1e9)
min_value = int(1e9)
def dfs(plus, minus, multiply, divide, count, result):
    global max_value
    global min_value
    if count == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)

    if plus > 0:
        dfs(plus - 1, minus, multiply, divide, count + 1, result + numbers[count])
    if minus > 0:
        dfs(plus, minus - 1, multiply, divide, count + 1, result - numbers[count])
    if multiply > 0:
        dfs(plus, minus, multiply - 1, divide, count + 1, result * numbers[count])
    if divide > 0:
        if result < 0:
            result = -(-result // numbers[count])
            dfs(plus, minus, multiply, divide - 1, count + 1, result)
        elif numbers[count] < 0:
            result = -(result // -numbers[count])
            dfs(plus, minus, multiply, divide - 1, count + 1, result)
        else:
            dfs(plus, minus, multiply, divide - 1, count + 1, result // numbers[count])


n = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
dfs(plus, minus, multiply, divide, 1, numbers[0])
print(max_value)
print(min_value)