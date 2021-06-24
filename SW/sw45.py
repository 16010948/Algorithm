T = int(input())

for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    print("#" + str(test_case), min(p * w, q if w < r else q + (w - r) * s))
