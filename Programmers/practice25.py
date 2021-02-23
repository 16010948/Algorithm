def solution(s):
    answer = True

    stack = []

    for bracket in s:
        if bracket == "(":
            stack.append(bracket)
        else:
            if len(stack) == 0:
                answer = False
                break

            b = stack.pop()
            if b != "(":
                answer = False
                break

    if len(stack) != 0:
        answer = False

    return answer

s = "()()"
# answer = True
print(solution(s))

s = "(())()"
# answer = True
print(solution(s))

s = ")()("
# answer = False
print(solution(s))

s = "(()("
# answer = False
print(solution(s))