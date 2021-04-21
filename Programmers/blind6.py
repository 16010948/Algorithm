def solution(dartResult):
    answer = 0
    score = ''
    scores = []

    for result in dartResult:
        if result == 'S':
            scores.append(int(score))
            scores[-1] **= 1
            score = ''
        elif result == 'D':
            scores.append(int(score))
            scores[-1] **= 2
            score = ''
        elif result == 'T':
            scores.append(int(score))
            scores[-1] **= 3
            score = ''
        elif result == '*':
            if len(scores) > 1:
                scores[-2] *= 2
            scores[-1] *= 2
        elif result == '#':
            scores[-1] *= -1
        else:
            score += result

    answer = sum(scores)

    return answer

dartResult = "1S2D*3T"
# answer = 37
print(solution(dartResult))

dartResult = "1D2S#10S"
# answer = 9
print(solution(dartResult))

dartResult = "1D2S0T"
# answer = 3
print(solution(dartResult))

dartResult = "1S*2T*3S"
# answer = 23
print(solution(dartResult))

dartResult = "1D#2S*3S"
# answer = 5
print(solution(dartResult))

dartResult = "1T2D3D#"
# answer = -4
print(solution(dartResult))

dartResult = "1D2S3T*"
# answer = 59
print(solution(dartResult))