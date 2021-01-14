# N이 1이 될 때까지 1을 빼거나 혹은 N을 k로 나누는 과정을 수행해야 하는 횟수의 최솟값
result = 0
# N, K를 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

while True:
    # N이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result -= 1
print(result)



