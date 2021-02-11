def quick_sort(array, start, end):
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and (len(array[pivot]) > len(array[left]) or (len(array[pivot]) == len(array[left]) and array[pivot] >= array[left])):
            left += 1
        while right > start and (len(array[pivot]) < len(array[right]) or (len(array[pivot]) == len(array[right]) and array[pivot] <= array[right])):
            right -= 1
        if left >= right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

n = int(input())
arr = []
for _ in range(n):
    word = input()
    if word not in arr:
       arr.append(word)
quick_sort(arr, 0, len(arr) - 1)

for word in arr:
    print(word)