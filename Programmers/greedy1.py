def solution(n, lost, reserve):
    answer = n

    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]

    for l in _lost:
        if l - 1 in _reserve:
            _reserve.remove(l - 1)
        elif l + 1 in _reserve:
            _reserve.remove(l + 1)
        else:
            answer -= 1

    return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
# answer = 5
print(solution(n, lost, reserve))

n = 5
lost = [2, 4]
reserve = [3]
# answer = 4
print(solution(n, lost, reserve))

n = 3
lost = [3]
reserve = [1]
# answer = 2
print(solution(n, lost, reserve))