T = 10

for test_case in range(1, T + 1):
    n = int(input())
    word = input()
    string = input()
    print("#{} {}".format(test_case, string.count(word)))