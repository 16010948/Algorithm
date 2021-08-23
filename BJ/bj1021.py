n, m = map(int, input().split())
values = list(map(int, input().split()))
queue = list(range(1, n + 1))

answer = 0
index = 0
for i in range(m):
    value_index = queue.index(values[i])
    answer += min(abs(value_index - index), abs(index + len(queue) - value_index), abs(value_index + len(queue) - index))
    index = value_index
    queue.pop(index)
print(answer)