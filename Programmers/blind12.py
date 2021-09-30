OVER = {
    10: "A", 11: "B", 12: "C",
    13: "D", 14: "E", 15: "F"
}


def parse(num, n):
    result = ""
    if num == 0:
        result = "0"
    while num > 0:
        remain = num % n
        if remain >= 10:
            remain = OVER[remain]
        else:
            remain = str(remain)
        result = remain + result
        num //= n
    return result


def solution(n, t, m, p):
    answer = ''

    i = 0
    total = ""
    while len(total) < m * t:
        total += parse(i, n)
        i += 1
    answer = total[p - 1::m][:t]
    return answer