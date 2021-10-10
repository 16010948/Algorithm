def file_sort(array):
    n = len(array)
    if n <= 1:
        return

    mid = n // 2
    g1 = array[:mid]
    g2 = array[mid:]
    file_sort(g1)
    file_sort(g2)

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        head1 = g1[i1]['head'].lower()
        head2 = g2[i2]['head'].lower()
        if head1 < head2:
            array[ia] = g1[i1]
            i1 += 1
        elif head1 == head2:
            number1 = int(g1[i1]['number'])
            number2 = int(g2[i2]['number'])
            if number1 <= number2:
                array[ia] = g1[i1]
                i1 += 1
            else:
                array[ia] = g2[i2]
                i2 += 1
        else:
            array[ia] = g2[i2]
            i2 += 1
        ia += 1

    for i in range(i1, len(g1)):
        array[ia] = g1[i]
        ia += 1
    for i in range(i2, len(g2)):
        array[ia] = g2[i]
        ia += 1


def solution(files):
    answer = []

    file_names = []
    for file in files:
        head = ''
        number = ''
        tail = ''
        for char in file:
            if tail == '' and char.isdigit():
                number += char
            elif number == '':
                head += char
            else:
                tail += char
        file_names.append({
            'file': file,
            'head': head,
            'number': number,
            'tail': tail
        })
    file_sort(file_names)
    for file_name in file_names:
        answer.append(file_name['file'])

    return answer