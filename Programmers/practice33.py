WEEK_DAYS = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]


def solution(a, b):
    answer = ''
    index = 5
    for i in range(1, a):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            index = (index + 3) % 7
        elif i != 2:
            index = (index + 2) % 7
        else:
            index = (index + 1) % 7

    index = (index + b - 1) % 7
    answer = WEEK_DAYS[index]
    return answer

a = 5
b = 24
# answer = "TUE"
print(solution(a, b))