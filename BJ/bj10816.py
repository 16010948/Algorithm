def bisect_left(array, start, end, target):
    while start < end:
        mid = (start + end) // 2
        if target <= array[mid]:
            end = mid
        else:
            start = mid + 1
    return end

def bisect_right(array, start, end, target):
    while start < end:
        mid = (start + end) // 2
        if target >= array[mid]:
            start = mid + 1
        else:
            end = mid
    return start

n = int(input())
card1 = list(map(int, input().split()))
card1.sort()

m = int(input())
card2 = list(map(int, input().split()))

for card_num in card2:
    index_left = bisect_left(card1, 0, n - 1, card_num)
    index_right = bisect_right(card1, 0, n - 1, card_num)
    count = index_right - index_left
    if card1[index_left] != card_num:
        print(0, end=" ")
    else:
        if index_right == n - 1:
            print(count + 1, end=" ")
        else:
            print(count, end=" ")