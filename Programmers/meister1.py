def solution(nums):
    answer = min(len(nums) // 2, len(list(set(nums))))
    return answer

nums = [3, 1, 2, 3]
# answer = 2
print(solution(nums))

nums = [3, 3, 3, 2, 2, 4]
# answer = 3
print(solution(nums))

nums = [3, 3, 3, 2, 2, 2]
# answer = 2
print(solution(nums))