iron = input()
answer = 0

stack = []
i = 0
while i < len(iron):
    if i < len(iron) - 1 and iron[i] == '(' and iron[i + 1] == ')':
        answer += len(stack)
        i += 1
    elif iron[i] == '(':
        stack.append(iron[i])
    else:
        answer += 1
        stack.pop()
    i += 1
print(answer)