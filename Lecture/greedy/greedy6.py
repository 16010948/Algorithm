# 나이트는 특정 위치에서
# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하거나
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동할 수 있음
# 나이트의 행 위치는 1 ~ 8, 열 위치는 a ~ h로 표현할 때 나이트가 이동할 수 있는 경우의 수

# 현재 나이트의 위치 입력
inputData = input()
row = int(inputData[1])
col = ord(inputData[0]) - ord('a') + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
count = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    nextRow = row + step[0]
    nextCol = col + step[1]
    # 해당 위치로 이동이 가능할 경우
    if 1 <= nextRow and nextRow <= 8 and 1 <= nextCol and nextCol <= 8:
        count += 1
print(count)