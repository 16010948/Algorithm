import math


def calc_gap(start, end):
    s_hour, s_min = map(int, start.split(':'))
    e_hour, e_min = map(int, end.split(':'))

    gap = (e_hour * 60 + e_min) - (s_hour * 60 + s_min)

    if gap < 0:
        gap *= -1

    return gap


def get_full_melody(melody, gap):
    time = 0
    full_melody = ''
    index = 0
    while time <= gap:
        full_melody += melody[index % len(melody)]
        index += 1
        if melody[index % len(melody)] != '#':
            time += 1
    return full_melody


def is_match(m, full_melody):
    if m not in full_melody:
        return False

    while m in full_melody:
        start = full_melody.index(m)
        end = start + len(m)
        if end == len(full_melody) or (end < len(full_melody) and full_melody[end] != '#'):
            return True
        full_melody = full_melody.replace(m, '', 1)
    return False


def solution(m, musicinfos):
    answer = '(None)'

    max_gap = 0
    length = len(m.replace('#', ''))
    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(',')
        gap = calc_gap(start, end)

        full_melody = get_full_melody(melody, gap)

        if gap < length:
            continue

        if is_match(m, full_melody):
            if gap > max_gap:
                answer = title
                max_gap = gap

    return answer