DWARF_COUNT = 9
FAKE_DWARF_COUNT = 2
HEIGHT_TOTAL = 100

def combination(start, flag, count, s):
    if s > gap:
        return

    if count == FAKE_DWARF_COUNT:
        if s == gap:
            for idx in range(DWARF_COUNT):
                if not flag[idx]:
                    print(dwarf[idx])
            exit(0)
        return

    for idx in range(start, DWARF_COUNT):
        flag[idx] = True
        combination(idx + 1, flag, count + 1, s + dwarf[idx])
        flag[idx] = False

total = 0
dwarf = []
for i in range(DWARF_COUNT):
    dwarf.append(int(input()))
    total += dwarf[-1]

gap = total - HEIGHT_TOTAL

flag = [False] * DWARF_COUNT
combination(0, flag, 0, 0)
