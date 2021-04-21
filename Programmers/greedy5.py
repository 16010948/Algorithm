def solution(name):
    answer = 0

    alpha_index = []
    for i in range(len(name)):
        answer += min(ord(name[i]) - ord('A'), (ord('Z') - ord(name[i])) + 1)
        if i != 0 and name[i] != 'A':
            alpha_index.append(i)

    curr = 0
    reverse_index = len(alpha_index) - 1
    index = 0
    reverse = False
    for i in range(len(alpha_index)):
        if not reverse:
            if alpha_index[index] - curr <= curr + len(name) - alpha_index[reverse_index]:
                answer += alpha_index[index] - curr
                curr = alpha_index[index]
                index += 1
            else:
                answer += curr + len(name) - alpha_index[reverse_index]
                curr = alpha_index[reverse_index]
                reverse_index -= 1
                reverse = True
        else:
            if curr - alpha_index[reverse_index] <= len(name) - curr + alpha_index[index]:
                answer += curr - alpha_index[reverse_index]
                curr = alpha_index[reverse_index]
                reverse_index -= 1
            else:
                answer += len(name) - curr + alpha_index[index]
                curr = alpha_index[index]
                index += 1
                reverse = False

    return answer

name = "JEROEN"
# answer = 56
print(solution(name))

name = "JAN"
# answer = 23
print(solution(name))