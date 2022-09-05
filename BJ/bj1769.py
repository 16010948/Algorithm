import sys
input = sys.stdin.readline

def problem(n, cnt):
    s = 0
    for i in range(len(n)):
        s += int(n[i])

    if s < 10:
        return [s, cnt + 1]
    else:
        return problem(str(s), cnt + 1)

x = input()[:-1]
cnt = 0
y = int(x)
if y >= 10:
    y, cnt = problem(x, cnt)

print(cnt)
print("YES" if y % 3 == 0 else "NO")