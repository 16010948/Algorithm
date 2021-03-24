def quick_sort(array):
    n = len(array)

    if n <= 1:
        return array
    pivot = array[-1]
    g1 = []
    g2 = []
    for i in range(n - 1):
        if array[i] < pivot:
            g1.append(array[i])
        else:
            g2.append(array[i])
    return quick_sort(g1) + [pivot] + quick_sort(g2)

n = int(input())

num = [0]
for _ in range(n):
    num.append(int(input()))

answer = set()
for i in range(1, n + 1):
    index = i
    tmp = set()
    visited = [False] * (n + 1)
    while not visited[index]:
        tmp.add(num[index])
        visited[index] = True
        index = num[index]
    if i == index:
        answer = answer | tmp

answer = quick_sort(list(answer))
print(len(answer))
for item in answer:
    print(item)