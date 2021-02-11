def bubble_sort(arr, last):
    if last > 0:
        for i in range(1, last + 1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        bubble_sort(arr, last - 1)

def print_array(arr):
    for data in arr:
        print(data, end=", ")
    print()

array = [3, 9, 4, 7, 5, 0, 1, 6, 8, 2]
print_array(array)
bubble_sort(array, len(array) - 1)
print_array(array)