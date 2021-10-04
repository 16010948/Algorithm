def binary_search(times, n):
    start = 1
    end = max(times) * n

    while start < end:
        mid = (start + end) // 2
        total = sum(mid // time for time in times)
        if total < n:
            start = mid + 1
        else:
            end = mid
    return start


def solution(n, times):
    answer = binary_search(times, n)
    return answer