n = int(input())
charge = list(map(int, input().split()))
y = 0
m = 0
for c in charge:
    y += ((c // 30) + 1) * 10
    m += ((c //  60) + 1) * 15
if y < m:
    print("Y", y)
elif y > m:
    print("M", m)
else:
    print("Y M", y)