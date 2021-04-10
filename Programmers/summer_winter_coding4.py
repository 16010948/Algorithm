def gcd(a, b):
    if b <= 0:
        return a
    return gcd(b, a % b)


def solution(w, h):
    answer = w * h - (w + h - gcd(w, h))

    return answer
w = 8
h = 12
# answer = 80
print(solution(w, h))