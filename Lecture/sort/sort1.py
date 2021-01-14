# 배열 A와 B의 원소를 k번 바꿔치기 하여
# 배열 A의 모든 원소의 합의 최댓값을 출력
def quickSort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quickSort(array, start, right - 1)
    quickSort(array, right + 1, end)

N, m = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

quickSort(array1, 0, N - 1)
quickSort(array2, 0, N - 1)

for i in range(m):
    if array1[i] < array2[N-i-1]:
        array1[i], array2[N-i-1] = array2[N-i-1], array1[i]
    else:
        break

print(sum(array1))