def solution(s):
    answer = True
    p_count = 0
    y_count = 0

    for c in s:
        if c == 'p' or c == 'P':
            p_count += 1
        if c == 'y' or c == 'Y':
            y_count += 1

    if p_count == y_count:
        answer = True
    else:
        answer = False

    return answer

s = "pPoooyY"
# answer = True
print(solution(s))

s = "Pyy"
# answer = False
print(solution(s))