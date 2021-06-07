T = int(input())

for test_case in range(1, T + 1):
    p = input().strip()
    q = input().strip()
    result = 'Y'
    if p + 'a' == q or p == q:
        result = 'N'
    print("#"+str(test_case), result)