def powerset(idx, interval):
    global count
    if idx == n:
        if interval == s:
            count += 1
        return
    powerset(idx + 1, interval + array[idx])
    powerset(idx + 1, interval)

n, s = map(int, input().split())
array = list(map(int, input().split()))

count = 0
powerset(0, 0)
if s == 0:
    count -= 1
print(count)