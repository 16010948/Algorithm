def solution(num):
    answer = 0

    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1
        answer += 1

        if answer > 500:
            answer = -1
            break

    return answer

n = 6
# answer = 8
print(solution(n))

n = 16
# answer = 4
print(solution(n))

n = 626331
# answer = -1
print(solution(n))