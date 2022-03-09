A = 'AAAA'
B = 'BB'

def polynomio(count):
    return A * (count // 4) + (B if count % 4 != 0 else '')

board = input() + ' '

count = 0
result = ''
for cur in board:
    if cur == 'X':
        count += 1
    else:
        if count % 2 == 0:
            result += polynomio(count) + cur
            count = 0
        else:
            result = -1
            break
print(result)