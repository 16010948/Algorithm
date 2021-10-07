def binary_search(array, target):
    start = 0
    end = max(array)
    while start <= end:
        mid = (start + end) // 2
        total = sum([tree - mid for tree in trees if tree > mid])
        if total >= target:
            start = mid + 1
        else:
            end = mid - 1
    return end

n, m = map(int, input().split())
trees = list(map(int, input().split()))

print(binary_search(trees, m))