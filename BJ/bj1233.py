s1, s2, s3 = map(int, input().split())

count = [0] * (s1 + s2 + s3 + 1)
answer = 0
max_count = 0
for c1 in range(1, s1 + 1):
    for c2 in range(1, s2 + 1):
        for c3 in range(1, s3 + 1):
            count[c1 + c2 + c3] += 1
            if count[c1 + c2 + c3] > max_count:
                max_count = count[c1 + c2 + c3]
                answer = c1 + c2 + c3

print(answer)