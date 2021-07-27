def parse_binary(n):
    b = ['0'] * 3
    for i in range(3 - 1, -1, -1):
        b[i] = str(n % 2)
        n //= 2
    return b

octal = input()

if octal == '0':
    print(0)
else:
    result = ""
    for i in range(len(octal)):
        result += "".join(parse_binary(int(octal[i])))
    print(result.lstrip("0"))