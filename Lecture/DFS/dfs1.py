# 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결된 것으로 간주
# N x M의 얼음 틀 모양이 주어질 때 생성되는 총 아이스크림의 개수

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x < 0 or y < 0 or x >= row or y >= col:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if iceFrame[x][y] == 0:
        # 해당 노드 방문 처리
        iceFrame[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

row, col = map(int, input().split())

iceFrame = []
for i in range(row):
    iceFrame.append(list(map(int, input())))

result = 0
for i in range(row):
    for j in range(col):
        if dfs(i, j) == True:
            result += 1

print(result)