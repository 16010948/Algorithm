scale = list(map(int, input().split()))

flag = 0
for i in range(1, 8):
    if scale[i - 1] > scale[i]:
        flag -= 1
    elif scale[i - 1] < scale[i]:
        flag += 1

if flag == 7:
    print("ascending")
elif flag == -7:
    print("descending")
else:
    print("mixed")