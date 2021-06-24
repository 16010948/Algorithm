def cal_area(rectangle):
    return (rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1])

def overlap(rectangles):
    overlap_rectangles = []
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if rectangles[i][2] > rectangles[j][0] and rectangles[i][3] > rectangles[j][1]:
                overlap_rectangles.append([max(rectangles[i][0], rectangles[j][0]), max(rectangles[i][1], rectangles[j][1]), rectangles[i][2], rectangles[i][3]])
    return overlap_rectangles

rectangles = []
area = 0
for _ in range(4):
    rectangles.append(list(map(int, input().split())))
    area += cal_area(rectangles[-1])

overlap_rectangles = overlap(rectangles)

for i in range(len(overlap_rectangles)):
    print(cal_area(overlap_rectangles[i]))
    area -= cal_area(overlap_rectangles[i])

overlap_rectangles = overlap(overlap_rectangles)

for i in range(len(overlap_rectangles)):
    area += cal_area(overlap_rectangles[i])
print(area)