def solution(left, right):
    answer = 0

    for n in range(left, right + 1):
        if n % (n ** 0.5) == 0:
            answer -= n
        else:
            answer += n

    return answer

left = 13
right = 17
# answer = 43
print(solution(left, right))

left = 24
right = 27
# answer = 52
print(solution(left, right))