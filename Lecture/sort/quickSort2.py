array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quickSort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]    # 피벗은 첫 번째 원소
    tail = array[1:]    # 피벗을 제외한 리스트

    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]
    return quickSort(leftSide) + [pivot] + quickSort(rightSide)

print(quickSort(array))