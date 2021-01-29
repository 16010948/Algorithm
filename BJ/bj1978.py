import math

answer = 0
n = int(input())
array = list(map(int, input().split()))

for item in array:
    flag = True
    for i in range(2, int(math.sqrt(item)) + 1):
        if item % i == 0:
            flag = False
            break
    if item > 1 and flag:
        answer += 1
print(answer)