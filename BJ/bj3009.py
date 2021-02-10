x_location = {}
y_location = {}

for _ in range(3):
    x, y = map(int, input().split())
    if x in x_location.keys():
        x_location[x] += 1
    else:
        x_location[x] = 1

    if y in y_location.keys():
        y_location[y] += 1
    else:
        y_location[y] = 1

for x in x_location.keys():
    if x_location[x] < 2:
        print(x, end=" ")
for y in y_location.keys():
    if y_location[y] < 2:
        print(y)