def convert_to_binary(n):
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result


def solution(s):
    answer = [0, 0]
    while s != '1':
        count = 0
        for i in s:
            if i == '0':
                count += 1
        length = len(s) - count
        s = convert_to_binary(length)
        answer[1] += count
        answer[0] += 1

    return answer

s = "110010101001"
# answer = [3, 8]
print(solution(s))

s = "01110"
# answer = [3, 3]
print(solution(s))

s = "1111111"
# answer = [4, 1]
print(solution(s))