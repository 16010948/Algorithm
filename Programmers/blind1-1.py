def combine(result, count, prev):
    if count == 1:
        result += prev
    else:
        result += str(count) + prev
    return result


def solution(s):
    answer = len(s)

    for i in range(1, len(s) + 1):
        prev = ""
        result = ""
        count = 1
        split = len(s) // i + 2 if len(s) % i != 0 else len(s) // i + 1
        for j in range(split):
            if prev == s[j * i: (j * i) + i]:
                count += 1
            else:
                result = combine(result, count, prev)
                prev = s[j * i: (j * i) + i]
                count = 1
        answer = min(answer, len(result))
    return answer