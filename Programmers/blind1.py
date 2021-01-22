def combine(result, count, string):
    if count <= 1:
        result += string
    else:
        result += str(count) + string
    return result

def solution(s):
    answer = 1000
    for i in range(len(s)):
        result = ''
        prev = ''
        count = 0
        for j in range(0, len(s), i+1):
            if prev == s[j:j+i+1]:
                count += 1
            else:
                result = combine(result, count, prev)
                prev = s[j:j+i+1]
                count = 1
        result = combine(result, count, prev)
        if answer > len(result):
            answer = len(result)
    return answer

s = "aabbaccc"
# answer = 7
print("#1", solution(s))

s = "ababcdcdababcdcd"
# answer = 9
print("#2", solution(s))

s = "abcabcdede"
# answer = 8
print("#3", solution(s))

s = "abcabcabcabcdededededede"
# answer = 14
print("#3", solution(s))

s = "xababcdcdababcdcd"
# answer = 17
print("#4", solution(s))