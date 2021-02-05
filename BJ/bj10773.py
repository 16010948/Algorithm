n = int(input())

stack = []
total = 0
for _ in range(n):
    value = int(input())
    if value == 0:
        total -= stack.pop()
    else:
        stack.append(value)
        total += value
print(total)