def bisect_left(array, start, end, target):
    while start < end:
        mid = (start + end) // 2
        if target <= array[mid]:
            end = mid
        else:
            start = mid + 1
    return end

n = int(input())
card1 = list(map(int, input().split()))
card1.sort()

m = int(input())
card2 = list(map(int, input().split()))

for card_num in card2:
    index = bisect_left(card1, 0, n - 1, card_num)
    count = 0
    while index < n and card1[index] == card_num:
        count += 1
        index += 1
    print(count, end=" ")