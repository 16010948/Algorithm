def reverse_bracket(u):
    reverse = ''
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            reverse += ')'
        else:
            reverse += '('
    return reverse


def correct_bracket(u):
    stack = []
    for bracket in u:
        if len(stack) > 0 and bracket == ')' and stack[-1] == '(':
            stack.pop()
        elif bracket == '(':
            stack.append(bracket)
        else:
            return False
    return True


def balanced_bracket(w):
    count = 0

    if len(w) == 0:
        return w
    for i, bracket in enumerate(w):
        if bracket == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            break
    u = w[:i + 1]
    if correct_bracket(u):
        v = balanced_bracket(w[i + 1:])
        return u + v
    else:
        return '(' + balanced_bracket(w[i + 1:]) + ')' + reverse_bracket(u)


def solution(p):
    answer = balanced_bracket(p)

    return answer

p = "(()())()"
# answer = "(()())()"
print(solution(p))

p = ")("
# answer = "()"
print(solution(p))

p = "()))((()"
# answer = "()(())()"
print(solution(p))