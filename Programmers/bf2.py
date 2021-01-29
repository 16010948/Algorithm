import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def make_combination(str1, str2):
    if str1 != "":
        if is_prime(int(str1)):
            prime.add(int(str1))

    for i in range(len(str2)):
        make_combination(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    answer = 0
    make_combination("", numbers)
    answer = len(prime)
    return answer

prime = set()
numbers = "17"
# answer = 3
print(solution(numbers))

prime = set()
numbers = "011"
# answer = 2
print(solution(numbers))