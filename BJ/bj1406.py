import sys
input = sys.stdin.readline

editor = input().rstrip()
l_stack = list(editor)
r_stack = []

n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "L" and len(l_stack) > 0:
        r_stack.append(l_stack.pop())
    elif command[0] == "D" and len(r_stack) > 0:
        l_stack.append(r_stack.pop())
    elif command[0] == "B" and len(l_stack) > 0:
        l_stack.pop()
    elif command[0] == "P":
        l_stack.append(command[1])
print(''.join(l_stack) + ''.join(r_stack[::-1]))