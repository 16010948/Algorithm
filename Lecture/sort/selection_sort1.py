def selection_sort(arr, start):
    if start < len(arr) - 1:
        min_index = start
        for i in range(start, len(arr) - 1):
            if arr[i] < arr[min_index]:
                min_index = i
        arr[start], arr[min_index] = arr[min_index], arr[start]
        selection_sort(arr, start + 1)

def print_array(arr):
    for data in arr:
        print(data, end=", ")
    print()

array = [3, 9, 4, 7, 5, 0, 1, 6, 8, 2]
print_array(array)
selection_sort(array, 0)
print_array(array)