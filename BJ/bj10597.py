def is_range(num):
    return 10 <= num and num <= max

def make_nums(n, idx, result, visited):
    if idx == length:
        print(' '.join(result))
        exit(0)

    if idx < length - 1:
        num = int(n[idx] + n[idx + 1])
        if is_range(num) and not visited[num]:
            visited[num] = True
            make_nums(n, idx + 2, result + [n[idx] + n[idx + 1]], visited)
            visited[num] = False

    num = int(n[idx])
    if num != 0 and not visited[num]:
        visited[num] = True
        make_nums(n, idx + 1, result + [n[idx]], visited)
        visited[num] = False

n = input()
length = len(n)

max = 0
if length < 10:
    max = length
else:
    max = (length - 9) // 2 + 9

visited = [False] * (max + 1)
make_nums(n, 0, [], visited)