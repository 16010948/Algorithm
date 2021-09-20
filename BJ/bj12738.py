def bisect_left(array, target):
    start = 0
    end = len(array)
    while start < end:
        mid = (start + end) // 2
        if target <= array[mid]:
            end = mid
        else:
            start = mid + 1
    return end

n = int(input())
arr = list(map(int, input().split()))

stack = []
for i in range(n):
    if len(stack) <= 0 or stack[-1] < arr[i]:
        stack.append(arr[i])
    else:
        index = bisect_left(stack, arr[i])
        stack[index] = arr[i]

print(len(stack))