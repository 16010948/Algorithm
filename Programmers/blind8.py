def parseBinary(number, length):
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    binary = '0' * (length - len(binary)) + binary
    return binary


def solution(n, arr1, arr2):
    answer = [''] * n

    for i in range(n):
        number1 = parseBinary(arr1[i], n)
        number2 = parseBinary(arr2[i], n)
        for j in range(n):
            if number1[j] == '1' or number2[j] == '1':
                answer[i] += '#'
            else:
                answer[i] += ' '

    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
# answer = ["#####","# # #", "### #", "# ##", "#####"]
print(solution(n, arr1, arr2))

n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
# answer = ["######", "### #", "## ##", " #### ", " #####", "### # "]
print(solution(n, arr1, arr2))