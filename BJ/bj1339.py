def parse_int(word, match):
    base = 1
    decimal = 0
    for i in range(len(word)):
        decimal += match[word[i]] * base
        base *= 10
    return decimal

n = int(input())

words = []
max_length = 0
for _ in range(n):
    words.append(input()[::-1])
    max_length = max(max_length, len(words[-1]))

alpha = {}
for i in range(max_length):
    for word in words:
        if len(word) > i:
            if word[i] in alpha:
                alpha[word[i]] += (10 ** i)
            else:
                alpha[word[i]] = 10 ** i
sorted_alpha = sorted(alpha.items(), key=(lambda x: x[1]), reverse=True)

match = {}
value = 9
for i in range(len(sorted_alpha)):
    match[sorted_alpha[i][0]] = value
    value -= 1

total = 0
for word in words:
    total += parse_int(word, match)
print(total)