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

def dfs(array):
    if len(array) == m:
        for data in array:
            print(data, end=" ")
        print()
        return

    for num in nums:
        array.append(num)
        dfs(array)
        array.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))
merge_sort(nums)
dfs([])