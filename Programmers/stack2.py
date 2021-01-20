import math


def solution(progresses, speeds):
    answer = []
    deploy = 0

    for i in range(len(progresses)):
        tmp = math.ceil((100 - progresses[i]) / speeds[i])
        if tmp > deploy:
            answer.append(1)
            deploy = tmp
        else:
            answer[len(answer) - 1] += 1
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
# answer = 	[2, 1]
print(solution(progresses, speeds))
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
# answer = 	[1, 3, 2]
print(solution(progresses, speeds))