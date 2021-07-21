def bisec_left(array, target, n):
    start = 0
    end = n
    while start < end:
        mid = (start + end) // 2
        if target > array[mid]:
            start = mid + 1
        else:
            end = mid
    return end
n = int(input())
arr = list(map(int, input().split()))

stack = []
length = -1
for i in range(n):
    if length < 0 or stack[length] < arr[i]:
        length += 1
        stack.append(arr[i])
    else:
        position = bisec_left(stack, arr[i], length)
        stack[position] = arr[i]
print(length + 1)