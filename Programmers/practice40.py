def hanoi(n, from_position, to_position, aux_position, result):
    if n == 1:
        result.append([from_position, to_position])
        return

    hanoi(n - 1, from_position, aux_position, to_position, result)
    result.append([from_position, to_position])
    hanoi(n - 1, aux_position, to_position, from_position, result)


def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer

n = 2
# answer = 	[[1, 2], [1, 3], [2, 3]]
print(solution(n))