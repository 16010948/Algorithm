def is_palindrome(palindrome):
    left = 0
    right = len(palindrome) - 1
    while left < right:
        if palindrome[left] != palindrome[right]:
            return False
        left += 1
        right -= 1
    return True


T = int(input())

for test_case in range(1, T + 1):
    palindrome = input()
    result = 1
    if not is_palindrome(palindrome):
        result = 0
    print("#{} {}".format(test_case, result))