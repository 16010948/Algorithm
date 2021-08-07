n = int(input())
num = list(map(int, input().split()))

count = {}
for i in range(n):
    if num[i] in count:
        count[num[i]] += 1
    else:
        count[num[i]] = 1

ngf = [-1] * n
stack = []
for i in range(n):
    while stack and count[num[stack[-1]]] < count[num[i]]:
        ngf[stack.pop()] = num[i]
    stack.append(i)

for i in range(n):
    print(ngf[i], end=" ")