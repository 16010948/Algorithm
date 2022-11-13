def permutation(arr):
    if len(arr) == n:
        print(' '.join([str(item) for item in arr]))
        return

    for i in range(1, n + 1):
        if not isSelected[i]:
            arr.append(i)
            isSelected[i] = True
            permutation(arr)
            arr.pop()
            isSelected[i] = False



n = int(input())

isSelected = [False] * (n + 1)
permutation([])