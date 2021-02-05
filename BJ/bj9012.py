n = int(input())

for _ in range(n):
    bracket = input()
    stack = []
    for b in bracket:
        if b == '(':
            stack.append(b)
        else:
            if len(stack) == 0:
                stack.append(b)
                break
            stack.pop()

    if len(stack) > 0:
        print("NO")
    else:
        print("YES")