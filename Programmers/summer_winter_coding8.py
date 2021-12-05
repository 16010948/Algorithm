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
    while i1 < len(g1) or i2 < len(g2):
        if i2 >= len(g2) or (i1 < len(g1) and g1[i1] > g2[i2]):
            array[ia] = g1[i1]
            i1 += 1
        else:
            array[ia] = g2[i2]
            i2 += 1
        ia += 1


def solution(A, B):
    answer = 0
    n = len(A)
    merge_sort(A)
    merge_sort(B)

    index = 0
    for a_num in A:
        if a_num < B[index]:
            answer += 1
            index += 1
    return answer