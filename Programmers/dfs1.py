def dfs(tickets, route, visited):
    if len(route) == len(tickets) + 1:
        return route

    ret = []
    for i, ticket in enumerate(tickets):
        if not visited[i] and ticket[0] == route[-1]:
            visited[i] = True
            ret = dfs(tickets, route + [ticket[1]], visited)
            if len(ret) == len(tickets) + 1:
                return ret
            visited[i] = False
    return route


def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    tickets.sort()
    answer = dfs(tickets, ["ICN"], visited)
    return answer