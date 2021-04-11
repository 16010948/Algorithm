def count_one(n):
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n //= 2
    return count


def solution(n):
    answer = 0
    n_ones = count_one(n)
    next_ones = 0

    while next_ones != n_ones:
        n += 1
        next_ones = count_one(n)

    answer = n

    return answer
n = 78
# answer = 83
print(solution(n))

n = 15
# answer = 23
print(solution(n))