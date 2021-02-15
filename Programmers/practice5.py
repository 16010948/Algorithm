from functools import reduce

def solution(arr):
    answer = 0
    total = reduce(lambda x, y: x+y, arr)
    answer = total / len(arr)
    return answer

arr = [1, 2, 3, 4]
# answer = 2.5
print(solution(arr))

arr = [5, 5]
# answer = 5
print(solution(arr))