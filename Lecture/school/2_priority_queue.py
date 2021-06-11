def selection_sort(n, array):
    for i in range(n):
        max_index = 0
        for j in range(1, n - i):
            if array[max_index] < array[j]:
                max_index = j
        array[n - i - 1], array[max_index] = array[max_index], array[n - i - 1]
        print(array)

def insertion_sort(n, array):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
            else:
                break

n = int(input())
array = list(map(int, input().split()))
#selection_sort(n, array)
insertion_sort(n, array)
print(array)