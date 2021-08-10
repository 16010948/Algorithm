PRIORITY = ('*/', '+-')
expression = input()

stack = []
for exp in expression:
    if exp.isalpha():
        print(exp, end="")
    else:
        if exp == '(':
            stack.append(exp)
        elif exp in PRIORITY[0]:
            while len(stack) > 0 and stack[-1] in PRIORITY[0]:
                print(stack.pop(), end="")
            stack.append(exp)
        elif exp in PRIORITY[1]:
            while len(stack) > 0 and stack[-1] in PRIORITY[0] + PRIORITY[1]:
                print(stack.pop(), end="")
            stack.append(exp)
        else:
            while len(stack) > 0:
                op = stack.pop()
                if op == '(':
                    break
                print(op, end="")

while len(stack) > 0:
    print(stack.pop(), end="")