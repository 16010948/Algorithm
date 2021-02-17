def bfs(n, computers, visited):
    visited[n] = True

    for i in range(len(computers[n])):
        if computers[n][i] == 1:
            if visited[i]:
                continue
            visited[i] = True
            bfs(i, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i]:
            continue
        bfs(i, computers, visited)
        answer += 1

    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# answer = 2
print(solution(n, computers))

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# answer = 1
print(solution(n, computers))