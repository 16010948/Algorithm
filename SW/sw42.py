T = 10

for test_case in range(1, T + 1):
    n, password = input().split()
    n = int(n)
    stack = []
    for p in password:
        if len(stack) > 0 and stack[-1] == p:
            stack.pop()
        else:
            stack.append(p)
    print("#{} {}".format(test_case, "".join(stack)))
