def solution(s):
    answer = ''
    half = (len(s) // 2)
    if len(s) % 2 == 1:
        answer = s[half]
    else:
        answer = s[half - 1: half + 1]
    return answer

s = "abcde"
# answer = "c"
print(solution(s))

s = "qwer"
# answer = "we"
print(solution(s))