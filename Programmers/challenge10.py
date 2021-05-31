def find_110(num):
    stack = []
    count = 0
    for i in range(len(num)):
        if len(stack) >= 2 and num[i] == '0' and stack[-2:] == ['1', '1']:
            count += 1
            stack.pop()
            stack.pop()
        else:
            stack.append(num[i])
    return (count, stack)


def find_111(num):
    if len(num) < 3:
        if "0" in num:
            return len(num)
        else:
            return 0
    else:
        for i in range(len(num) - 2):
            if num[i] + num[i + 1] + num[i + 2] == "111":
                return i
        return len(num)


def solution(s):
    answer = []

    for num in s:
        count, stack = find_110(num)
        index = find_111("".join(stack) + "110" * count)
        for _ in range(count):
            stack.insert(index, "110")
        answer.append("".join(stack))

    return answer

s = ["1110", "100111100", "0111111010"]
# answer = 	["1101", "100110110", "0110110111"]
print(solution(s))