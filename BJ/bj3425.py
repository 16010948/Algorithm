INF = 10**9
def start(commands, num):
    stack = [num]
    for command in commands:
        if command[:3] == "NUM":
            n = int(command[4:])
            stack.append(n)
        elif command == "POP":
            if len(stack) < 1:
                return "ERROR"
            stack.pop()
        elif command == "INV":
            if len(stack) < 1:
                return "ERROR"
            stack[-1] *= -1
        elif command == "DUP":
            if len(stack) < 1:
                return "ERROR"
            stack.append(stack[-1])
        elif command == "SWP":
            if len(stack) < 2:
                return "ERROR"
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif command == "ADD":
            if len(stack) < 2:
                return "ERROR"
            a = stack.pop()
            b = stack.pop()
            result = b + a
            if abs(result) > INF:
                return "ERROR"
            stack.append(result)
        elif command == "SUB":
            if len(stack) < 2:
                return "ERROR"
            a = stack.pop()
            b = stack.pop()
            result = b - a
            if abs(result) > INF:
                return "ERROR"
            stack.append(result)
        elif command == "MUL":
            if len(stack) < 2:
                return "ERROR"
            a = stack.pop()
            b = stack.pop()
            result = b * a
            if abs(result) > INF:
                return "ERROR"
            stack.append(result)
        elif command == "DIV":
            if len(stack) < 2:
                return "ERROR"
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                return "ERROR"
            result = abs(b) // abs(a)
            if (a > 0 and b < 0) or (a < 0 and b > 0):
                result *= -1
            stack.append(result)
        elif command == "MOD":
            if len(stack) < 2:
                return "ERROR"
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                return "ERROR"
            result = abs(b) % abs(a)
            if b < 0:
                result *= -1
            stack.append(result)

    if len(stack) == 1:
        return stack[0]
    return "ERROR"

commands = []
nums = []

while True:
    command = input().strip()
    if command == "QUIT":
        break
    elif command == "END":
        n = int(input())
        for _ in range(n):
            num = int(input())
            print(start(commands, num))
        print()
        input()

        commands = []
    else:
        commands.append(command)