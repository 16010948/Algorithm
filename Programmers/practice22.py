def solution(seoul):
    answer = "김서방은 " + str(seoul.index("Kim")) + "에 있다"

    return answer

seoul = ["Jane", "Kim"]
# answer = "김서방은 1에 있다"
print(solution(seoul))