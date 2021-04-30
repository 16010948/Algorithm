def step_stone(mid, stones, k):
    count = 0
    for stone in stones:
        if stone - mid <= 0:
            count += 1
        else:
            count = 0
        if count >= k:
            return True
    return False


def solution(stones, k):
    answer = 0

    left, right = min(stones), max(stones)
    while left <= right:
        mid = (left + right) // 2
        if step_stone(mid, stones, k):
            right = mid - 1
        else:
            left = mid + 1

    answer = left
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
# answer = 3
print(solution(stones, k))
