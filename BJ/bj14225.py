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

def powerset(idx, s):
    if idx == n:
        result.append(s)
        return
    powerset(idx + 1, s)
    powerset(idx + 1, s + nums[idx])

n = int(input())
nums = list(map(int, input().split()))

result = []
powerset(0, 0)


result = list(set(result))
merge_sort(result)
answer = result[-1] + 1
for i in range(1, len(result)):
    if i != result[i]:
        answer = i
        break

print(answer)