def solution(n, s):
    if s // n <= 0:
        answer = [-1]
    else:
        answer = [s // n] * n
        for i in range(s % n):
            answer[n - i - 1] += 1

    return answer

n = 2
s = 9
# answer = [4, 5]
print(solution(n, s))

n = 2
s = 1
# answer = [-1]
print(solution(n, s))

n = 2
s = 8
# answer = [4, 4]
print(solution(n, s))