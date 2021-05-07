def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while right > start and array[pivot] <= array[right]:
            right -= 1

        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

n = int(input())
fear = list(map(int, input().split()))
quick_sort(fear, 0, n - 1)

count = 0
answer = 0
for i in range(n):
    count += 1
    if count >= fear[i]:
        count = 0
        answer += 1
print(answer)