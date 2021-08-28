vowel = ('a', 'e', 'i', 'o', 'u')

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
    while i1 < len(g1) or i2 < len(g2):
        if i2 >= len(g2) or (i1 < len(g1) and g1[i1] < g2[i2]):
            array[ia] = g1[i1]
            i1 += 1
        else:
            array[ia] = g2[i2]
            i2 += 1
        ia += 1

def combination(array, start, c_count, v_count, result):
    if len(result) == n:
        if c_count >= 2 and v_count >= 1:
            result = list(result)
            merge_sort(result)
            password.append("".join(result))
        return
    for i in range(start, len(array)):
        if array[i] in vowel:
            combination(array, i + 1, c_count, v_count + 1, result + array[i])
        else:
            combination(array, i + 1, c_count + 1, v_count, result + array[i])

n, m = map(int, input().split())
character = list(input().split())

password = []
combination(character, 0, 0, 0, "")
merge_sort(password)
for p in password:
    print(p)
