def rank_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end\
                and (array[left][1] > array[pivot][1]\
                or (array[left][1] == array[pivot][1] and array[left][2] > array[pivot][2])\
                or (array[left][1] == array[pivot][1] and array[left][2] == array[pivot][2] and array[left][3] >= array[pivot][3])):
            left += 1
        while right > start\
                and (array[right][1] < array[pivot][1]\
                or (array[right][1] == array[pivot][1] and array[right][2] < array[pivot][2])\
                or (array[right][1] == array[pivot][1] and array[right][2] == array[pivot][2] and array[right][3] <= array[pivot][3])):
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    rank_sort(array, start, right - 1)
    rank_sort(array, right + 1, end)

n, k = map(int, input().split())
medal = []
for _ in range(n):
    medal.append(list(map(int, input().split())))
rank_sort(medal, 0, n - 1)

rank = 0
pivot = [0, 0, 0]
for i in range(n):
    if pivot[0] != medal[i][1] or pivot[1] != medal[i][2] or pivot[2] != medal[i][3]:
        rank = i + 1
        pivot = medal[i][1:]
    if k == medal[i][0]:
        break
print(rank)