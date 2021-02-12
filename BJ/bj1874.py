n = int(input())

result = ''
total = 1
stack = []
for _ in range(n):
    i = int(input())
    if len(stack) > 0 and i < stack[-1]:
        while len(stack) > 0 and stack[-1] > i:
            stack.pop()
            result += '-'
    else:
        for j in range(total, i + 1):
            stack.append(j)
            result += '+'
        total = max(total, i + 1)
    if len(stack) == 0 or stack[-1] != i:
        result = "NO"
        break
    stack.pop()
    result += '-'

if result == "NO":
    print(result)
else:
    for r in result:
        print(r)