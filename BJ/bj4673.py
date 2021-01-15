def self_number(n):
    if n < 10:
        return n
    else:
        return (n % 10) + self_number(n//10)

array = []
for x in range(1, 10001):
    x += self_number(x)
    array.append(x)

for x in range(1, 10001):
    if x not in array:
        print(x)

