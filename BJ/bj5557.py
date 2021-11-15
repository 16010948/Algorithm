def combination(s, idx):
    global answer
    if s < 0 or s > 20:
        return

    if idx == n - 1:
        if s == nums[idx]:
           answer += 1
        return
    combination(s + nums[idx], idx + 1)
    combination(s - nums[idx], idx + 1)

n = int(input())
nums = list(map(int, input().split()))

answer = 0
combination(nums[0], 1)
print(answer)