def check_palindrome(string, result):
    if result >= 2:
        return 2

    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            result = min(check_palindrome(string[:i] + string[i + 1:], result + 1), check_palindrome(string[:length - i - 1] + string[length - i:], result + 1))
            break
    return result

n = int(input())

for _ in range(n):
    string = input()
    print(check_palindrome(string, 0))
