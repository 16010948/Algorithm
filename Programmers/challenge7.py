def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer += absolutes[i] * -1

    return answer

absolutes = [4, 7, 12]
signs = [True, False, True]
# answer = 9
print(solution(absolutes, signs))

absolutes = [1, 2, 3]
signs = [False, False, True]
# answer = 0
print(solution(absolutes, signs))