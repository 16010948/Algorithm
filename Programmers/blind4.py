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
        if type(g1[i1]) == tuple:
            if g1[i1][1] > g2[i2][1] or (g1[i1][1] == g2[i2][1] and g1[i1][0] < g2[i2][0]):
                array[ia] = g1[i1]
                i1 += 1
            else:
                array[ia] = g2[i2]
                i2 += 1
        else:
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


def bisec_right(array, start, end, target):
    while start < end:
        mid = (start + end) // 2
        if target >= array[mid]:
            start = mid + 1
        else:
            end = mid
    return start


def solution(N, stages):
    answer = []
    clear = len(stages)
    merge_sort(stages)
    left = 0
    count = 0
    rates = []
    for i in range(1, N + 1):
        right = bisec_right(stages, 0, clear, i)
        if right == 0:
            count = 0
        elif stages[right - 1] == i:
            count = right - left
        else:
            count = 0
        if clear - left == 0:
            rate = 0
        else:
            rate = count / (clear - left)
        rates.append((i, rate))
        left = right
    merge_sort(rates)

    for i in range(N):
        answer.append(rates[i][0])

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# answer = [3, 4, 2, 1, 5]
print(solution(N, stages))

N = 4
stages = [4, 4, 4, 4, 4]
# answer = [4,1,2,3]
print(solution(N, stages))