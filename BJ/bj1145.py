INF = int(1e10)

def gcd(a ,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcd(array):
    result = array[0]
    for i in range(1, len(array)):
        result = (result * array[i]) // gcd(result, array[i])
    return result

def dfs(array, start):
    if len(array) == 3:
        return lcd(array)

    min_value = INF
    for i in range(start, 5):
        min_value = min(min_value, dfs(array + [nums[i]], i + 1))
    return min_value

nums = list(map(int, input().split()))

print(dfs([], 0))