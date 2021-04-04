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


def solution(d, budget):
    answer = -1
    merge_sort(d)
    total = 0
    for i in range(len(d)):
        total += d[i]
        if total > budget:
            answer = i
            break

    if answer < 0:
        answer = len(d)

    return answer

d = [1, 3, 2, 5, 4]
budget = 9
# answer = 3
print(solution(d, budget))

d = [2, 2, 3, 3]
budget = 10
# answer = 4
print(solution(d, budget))