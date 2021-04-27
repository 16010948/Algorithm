def solution(s):
    answer = 0

    for i in range(len(s)):
        stack = []
        for bracket in s:
            if bracket == '[' or bracket == '{' or bracket == '(':
                stack.append(bracket)
            elif len(stack) > 0 and stack[-1] == '[' and bracket == ']':
                stack.pop()
            elif len(stack) > 0 and stack[-1] == '{' and bracket == '}':
                stack.pop()
            elif len(stack) > 0 and stack[-1] == '(' and bracket == ')':
                stack.pop()
            else:
                stack.append(bracket)
                break
        if len(stack) == 0:
            answer += 1
        s = s[1:] + s[0]

    return answer

s = "[](){}"
# answer = 3
print(solution(s))

s = "}]()[{"
# answer = 2
print(solution(s))

s = "[)(]"
# answer = 0
print(solution(s))

s = "}}}"
# answer = 0
print(solution(s))