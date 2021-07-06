T = int(input())

for test_case in range(1, T + 1):
    string = input()
    for i in range(1, 10 + 1):
        if string == (string[:i] * ((30 // i) + 1))[:30]:
            print("#%d %d"%(test_case, i))
            break