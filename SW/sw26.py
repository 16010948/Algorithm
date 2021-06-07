T = int(input())

for test_case in range(1, T + 1):
    s = input()
    result = ""
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'b':
            result += 'd'
        elif s[i] == 'd':
            result += 'b'
        elif s[i] == 'p':
            result += 'q'
        elif s[i] == 'q':
            result += 'p'
    print("#"+str(test_case), result)