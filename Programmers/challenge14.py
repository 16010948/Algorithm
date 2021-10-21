def solution(n, left, right):
    answer = []

    start_y = left // n + 1
    end_y = right // n + 1

    start_x = left % n + 1
    end_x = n + 1
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x):
            answer.append(max(y, x))
            if len(answer) == right - left + 1:
                break
        start_x = 1

    return answer