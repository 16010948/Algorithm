def percentage(x, y):
    return (y * 100) // x

def bisect_left(target):
    global answer
    start = 1
    end = 1_000_000_000

    while start <= end:
        mid = (start + end) // 2
        new_z = percentage(x + mid, y + mid)
        if new_z >= target:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    return answer

x, y = map(int, input().split())
z = percentage(x, y)

answer = -1
if z >= 99:
    print(-1)
else:
    print(bisect_left(z + 1))