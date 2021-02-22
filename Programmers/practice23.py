def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solution(arr):
    answer = 1

    while len(arr) > 1:
        gcd_front = gcd(arr[-1], arr[-2])
        answer = (arr.pop() * arr.pop()) // gcd_front
        arr.insert(0, answer)

    return answer

arr = [2, 6, 8, 14]
# answer = 168
print(solution(arr))

arr = [1,2,3]
# answer = 6
print(solution(arr))