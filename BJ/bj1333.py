n, l, d = map(int, input().split())

total = n * (l + 5) - 5
answer = ((total // d) + 1) * d

i = 1
while i * d <= total:
    call = (i * d) % (l + 5)
    if l <= call and call < l + 5:
        answer = i * d
        break
    i += 1

print(answer)