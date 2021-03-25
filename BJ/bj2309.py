dwarf = []
for _ in range(9):
    dwarf.append(int(input()))
gap = sum(dwarf) - 100
for i in range(len(dwarf)):
    for j in range(i + 1, len(dwarf)):
        if dwarf[i] + dwarf[j] == gap:
            dwarf[i] = -1
            dwarf[j] = -1
            break
    if dwarf[i] == -1:
        break
dwarf.sort()
for i in range(2, len(dwarf)):
    print(dwarf[i])