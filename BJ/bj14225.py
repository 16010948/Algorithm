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
        answer.append(s)
        return
    powerset(idx + 1, s)
    powerset(idx + 1, s + nums[idx])

n = int(input())
nums = list(map(int, input().split()))

answer = []
powerset(0, 0)


answer = list(set(answer))
merge_sort(answer)
is_exist = False
for i in range(1, len(answer)):
    if i != answer[i]:
        print(i)
        is_exist = True
        break

if not is_exist:
    print(answer[-1] + 1)