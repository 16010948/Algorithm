ARRAY = '1213'
n = int(input())

answer = ARRAY * (n // len(ARRAY)) + ARRAY[:(n % len(ARRAY))]
print(answer)