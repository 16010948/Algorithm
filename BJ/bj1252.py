def operate_bit(bit1, bit2):
    global carriage
    sum_bit = carriage + bit1 + bit2
    if carriage + bit1 + bit2 > 1:
        result = str(sum_bit - 2)
        carriage = 1
    else:
        result = str(sum_bit)
        carriage = 0
    return result

binary1, binary2 = map(list, input().split())

binary1 = list(map(int, binary1))
binary2 = list(map(int, binary2))

i1 = len(binary1) - 1
i2 = len(binary2) - 1
carriage = 0
result = [''] * (max(i1 + 1, i2 + 1) + 1)
while i1 >= 0 and i2 >= 0:
    result[max(i1, i2) + 1] = operate_bit(binary1[i1], binary2[i2])
    i1 -= 1
    i2 -= 1

for i in range(i1, -1, -1):
    result[i + 1] = operate_bit(binary1[i], 0)

for i in range(i2, -1, -1):
    result[i + 1] = operate_bit(binary2[i], 0)

if carriage != 0:
    result[0] = '1'
else:
    for i in range(len(result) - 1):
        if result[i] == '1':
            break
        result[i] = ''
print(''.join(result))