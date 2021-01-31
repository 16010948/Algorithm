def solution(number, k):
    answer = ''
    stack = []

    for n in number:
        while k != 0 and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    answer = ''.join(stack[:len(stack) - k])
    return answer

number = "1924"
k = 2
# answer = "94"
print(solution(number, k))

number = "1231234"
k = 3
# answer = "3234"
print(solution(number, k))

number = "4177252841"
k = 4
# answer = "775841"
print(solution(number, k))