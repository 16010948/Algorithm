n = input()

decimal = 0
base = 1
for i in range(len(n) - 1, -1, -1):
    if n[i].isalpha():
        decimal += (ord(n[i]) - ord('A') + 10) * base
    else:
        decimal += int(n[i]) * base
    base *= 16
print(decimal)