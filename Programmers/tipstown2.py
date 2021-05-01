def solution(s):
    answer = 0
    stack = []

    for char in s:
        if len(stack) == 0 or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()

    answer = 1 if len(stack) == 0 else 0

    return answer

s = "baabaa"
# answer = 1
print(solution(s))

s = "cdcd"
# answer = 0
print(solution(s))