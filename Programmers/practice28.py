def solution(s):
    answer = ''

    index = 0
    for c in s:
        if c == " ":
            index = 0
        elif index % 2 == 0:
            c = c.upper()
            index += 1
        else:
            c = c.lower()
            index += 1
        answer += c

    return answer

s = "try hello world"
# answer = "TrY HeLlO WoRlD"
print(solution(s))