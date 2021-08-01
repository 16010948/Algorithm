def merge_sort(array):
    length = len(array)
    if length <= 1:
        return
    mid = length // 2
    g1 = array[:mid]
    g2 = array[mid:]
    merge_sort(g1)
    merge_sort(g2)

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            array[ia] = g1[i1]
            i1 += 1
        else:
            array[ia] = g2[i2]
            i2 += 1
        ia += 1

    for i in range(i1, len(g1)):
        array[ia] = g1[i]
        ia += 1
    for i in range(i2, len(g2)):
        array[ia] = g2[i]
        ia += 1

def count_char(name, char):
    count = 0
    for c in name:
        if c == char:
            count += 1
    return count

LOVE = ('L', 'O', 'V', 'E')
ohminsik = input()
n = int(input())

count = []
for char in LOVE:
    count.append(count_char(ohminsik,  char))
max_percent = -1
answers = []
for _ in range(n):
    name = input()
    tmp_count = []
    for index in range(len(LOVE)):
        tmp_count.append(count[index] + count_char(name, LOVE[index]))

    percent = 1
    for i in range(len(count)):
        for j in range(i + 1, len(count)):
            percent *= tmp_count[i] + tmp_count[j]
    percent %= 100

    if percent > max_percent:
        max_percent = percent
        answers = [name]
    elif percent == max_percent:
        answers.append(name)
merge_sort(answers)
print(answers[0])