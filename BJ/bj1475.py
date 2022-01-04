room = input()
length = len(room)

number = [[False] * 10 for _ in range(length)]

count = 1
for i in range(length):
    for j in range(length):
        if not number[j][int(room[i])]:
            number[j][int(room[i])] = True
            count = max(count, j + 1)
            break
        elif room[i] == '6' and not number[j][9]:
            number[j][9] = True
            count = max(count, j + 1)
            break
        elif room[i] == '9' and not number[j][6]:
            number[j][6] = True
            count = max(count, j + 1)
            break
print(count)