n, k = map(int, input().split())
Josephus = list(range(1, n + 1))
result = "<"
index = 0
while Josephus:
    index = (index + (k - 1)) % len(Josephus)
    result +=str(Josephus.pop(index)) +", "

result = result[:-2] + ">"
print(result)