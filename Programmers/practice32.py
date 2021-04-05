def solution(x, n):
    answer = []

    for i in range(n):
        answer.append(x + x * i)

    return answer
x = 2
n = 5
# answer = 	[2, 4, 6, 8, 10]
print(solution(x, n))

x = 4
n = 3
# answer = 	[4, 8, 12]
print(solution(x, n))

x = -4
n = 2
# answer = 	[-4, -8]
print(solution(x, n))