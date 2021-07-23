n = int(input())

file = []
for _ in range(n):
    file.append(list(input()))

length = len(file[0])
for i in range(length):
    for j in range(1, n):
        if file[0][i] != file[j][i]:
            file[0][i] = "?"
            break
print("".join(file[0]))