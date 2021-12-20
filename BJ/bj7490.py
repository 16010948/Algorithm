def combination(idx, operations, n):
    if idx == n:
        expression = ''
        for i in range(1, n + 1):
            if i < n:
                expression += str(i) + operations[i - 1]
            else:
                expression += str(i)
        if eval(expression.replace(' ', '')) == 0:
            answers.append(expression)
        return
    combination(idx + 1, operations + ['+'], n)
    combination(idx + 1, operations + ['-'], n)
    combination(idx + 1, operations + [' '], n)

tc = int(input())

answers = []
for _ in range(tc):
    n = int(input())
    answers = []
    combination(1, [], n)
    for e in sorted(answers):
        print(e)
    print()