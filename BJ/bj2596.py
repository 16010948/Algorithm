def check_alpha(alpha, character):
    count = 0
    for i in range(6):
        if alpha[i] != character[i]:
            count += 1
        if count > 1:
            return False
    return True

ALPHA = {
    'A': '000000',
    'B': '001111',
    'C': '010011',
    'D': '011100',
    'E': '100110',
    'F': '101001',
    'G': '110101',
    'H': '111010'
}

n = int(input())
string = input()
answer = ''
for i in range(n):
    character = ''
    for key in ALPHA.keys():
        if check_alpha(ALPHA[key], string[i * 6: i * 6 + 6 + 1]):
            character = key
            break
    if character == '':
        answer = i + 1
        break
    answer += character
print(answer)
