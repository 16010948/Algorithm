def solution(sizes):
    max_longer = 0
    max_shorter = 0
    for width, height in sizes:
        longer = max(width, height)
        shorter = min(width, height)
        max_longer = max(max_longer, longer)
        max_shorter = max(max_shorter, shorter)

    answer = max_longer * max_shorter

    return answer