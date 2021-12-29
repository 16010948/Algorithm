class File:
    def __init__(self, head, number, tail, origin):
        self.head = head
        self.number = int(number)
        self.tail = tail
        self.origin = origin


def solution(files):
    answer = []

    splited_files = []
    for idx, file in enumerate(files):
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
        splited_files.append(File(head, number, tail, file))
    splited_files.sort(key=lambda f: (f.head.lower(), f.number))

    for file in splited_files:
        answer.append(file.origin)

    return answer