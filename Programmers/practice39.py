def solution(s, n):
    answer = ''

    for c in s:
        if c.islower():
            caesar = chr(ord(c) + n)
            if not caesar.islower():
                caesar = chr(ord(caesar) - ord('z') + ord('a') - 1)
            answer += caesar
        elif c.isupper():
            caesar = chr(ord(c) + n)
            if not caesar.isupper():
                caesar = chr(ord(caesar) - ord('Z') + ord('A') - 1)
            answer += caesar
        else:
            answer += c

    return answer

s = "AB"
n = 1
# answer = "BC"
print(solution(s, n))

s = "z"
n = 1
# answer = "a"
print(solution(s, n))

s = "a B z"
n = 4
# answer = "e F d"
print(solution(s, n))