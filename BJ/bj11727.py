n = int(input())

num1 = 2
num2 = 1
count = 1

for i in range(2, n + 1):
    count = num1 + num2
    num2 = num1
    num1 = count

print(count % 10007)