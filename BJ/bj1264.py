vowel = ('a', 'e', 'i', 'o', 'u')
while True:
    string = input().lower()
    if string == "#":
        break

    count = 0
    for ch in string:
        if ch in vowel:
            count += 1
    print(count)