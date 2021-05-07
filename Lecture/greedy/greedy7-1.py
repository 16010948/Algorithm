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

string = input()

number = 0
result = []
for char in string:
    if char.isdigit():
        number += int(char)
    else:
        result.append(char)
quick_sort(result, 0, len(result) - 1)

if number != 0:
    result.append(str(number))
print(''.join(result))