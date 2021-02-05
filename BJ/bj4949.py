BRACKET = {')': '(', ']':'['}
string = " "
while True:
    string = input()
    stack = []

    if string == ".":
        break

    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s in BRACKET.keys():
            if len(stack) == 0:
                stack.append(s)
                break
            else:
                b = stack.pop()
                if b != BRACKET[s]:
                    stack.append(s)
                    break
    if len(stack) != 0:
        print("no")
    else:
        print("yes")