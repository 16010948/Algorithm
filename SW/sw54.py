T = int(input())

for test_case in range(1, T + 1):
    result = input().replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
    print("#%d %s"%(test_case, result))