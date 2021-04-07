def solution(x):
    answer = True
    total = 0
    tmp = x
    while tmp > 0:
        total += tmp % 10
        tmp //= 10

    if x % total != 0:
        answer = False

    return answer

x = 10
# answer = true
print(solution(x))

x = 12
# answer = true
print(solution(x))

x = 11
# answer = false
print(solution(x))

x = 13
# answer = false
print(solution(x))