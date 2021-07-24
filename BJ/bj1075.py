n = int(input())
f = int(input())

for last in range(100):
    if ((n // 100) * 100 + last) % f == 0:
        print("{:02d}".format(last))
        break