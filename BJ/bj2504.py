brackets = input()

stack = []
tmp = 1
answer = 0
for idx, bracket in enumerate(brackets):
    if bracket == '(':
        tmp *= 2
        stack.append(bracket)
    elif bracket == '[':
        tmp *= 3
        stack.append(bracket)
    elif len(stack) > 0:
        open = stack.pop()
        if bracket == ')' and open == '(':
            if brackets[idx - 1] == '(':
                answer += tmp
            tmp //= 2
        elif bracket == ']' and open == '[':
            if brackets[idx - 1] == '[':
                answer += tmp
            tmp //= 3

        else:
            answer = 0
            break
    else:
        answer = 0
        break

if len(stack) != 0:
    print(0)
else:
    print(answer)