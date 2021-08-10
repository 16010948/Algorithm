string = input()
alpha = [0] * (ord('z') - ord('a') + 1)

for ch in string:
    alpha[ord(ch) - ord('a')] += 1

for count in alpha:
    print(count, end=" ")