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


def solution(phone_book):
    answer = True
    quick_sort(phone_book, 0, len(phone_book) - 1)

    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i - 1]):
            answer = False
            break

    return answer

phone_book = ["119", "97674223", "1195524421"]
# answer = False
print("#1", solution(phone_book))

phone_book = ["123", "456", "789"]
# answer = True
print("#1", solution(phone_book))

phone_book = ["12", "123", "1235", "567", "88"]
# answer = False
print("#1", solution(phone_book))