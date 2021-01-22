def solution(n):
    answer = 1
    tile1 = 1
    for _ in range(1, n):
        tile2 = answer
        answer = (answer + tile1) % 1000000007
        tile1 = tile2
    return answer
n = 4
# answer = 5
print(solution(n))