def solution(s):
    answer = ''
    JadenCase = s.split(' ')

    for i in range(len(JadenCase)):
        if len(JadenCase[i]) > 0 and JadenCase[i][0].isalpha():
            JadenCase[i] = JadenCase[i][0].upper() + JadenCase[i][1:].lower()
        else:
            JadenCase[i] = JadenCase[i].lower()
    answer = ' '.join(JadenCase)

    return answer
s = "3people unFollowed me"
# answer = "3people Unfollowed Me"
print(solution(s))

s = "for the last week"
# answer = 	"For The Last Week"
print(solution(s))