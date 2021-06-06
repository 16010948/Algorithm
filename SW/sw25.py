def merge_sort(array):
    n = len(array)
    if n <= 1:
        return
    mid = n // 2
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


T = int(input())
for test_case in range(1, T + 1):
    string = input()
    dictionary = {}
    for char in string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    odd_char = []
    for key in dictionary:
        if dictionary[key] % 2 == 1:
            odd_char.append(key)

    if len(odd_char) == 0:
        result = "Good"
    else:
        merge_sort(odd_char)
        result = "".join(odd_char)
    print("#" + str(test_case), result)
