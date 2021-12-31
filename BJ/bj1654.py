def binary_search():
    global answer
    start = 1
    end = max_c

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for c in cable:
            cnt += c // mid

        if cnt >= n:
            start = mid + 1
            answer = max(answer, mid)
        else:
            end = mid - 1

answer = 0
k, n = map(int, input().split())

cable = []
max_c = 0
for _ in range(k):
    cable.append(int(input()))
    max_c = max(max_c, cable[-1])
binary_search()
print(answer)