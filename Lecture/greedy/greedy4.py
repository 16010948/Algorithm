# 여행가가 최종적으로 도착할 지점의 좌표 출력
N = int(input())
plans = input().split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
MOVE_TYPES = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(MOVE_TYPES)):
        if plan == MOVE_TYPES[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny

print(x, y)