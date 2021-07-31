while True:
    n = input()
    if n == '0':
        break

    result = "yes"
    for i in range(len(n) // 2):
        if n[i] != n[len(n) - i - 1]:
            result = "no"
            break
    print(result)