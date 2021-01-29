def solution(brown, yellow):
    answer = []

    b = brown // 2 - 2
    for i in range(1, b):
        if (b - i) * i == yellow:
            answer = [(b - i + 2), i + 2]
            break

    return answer

brown = 10
yellow = 2
# answer = [4, 3]
print(solution(brown, yellow))

brown = 8
yellow = 1
# answer = [3, 3]
print(solution(brown, yellow))

brown = 24
yellow = 24
# answer = [8, 6]
print(solution(brown, yellow))
