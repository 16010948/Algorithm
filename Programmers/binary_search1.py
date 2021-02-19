def binary_search(times, n, start, end):
    while start < end:
        mid = (start + end) // 2
        total = sum(mid // time for time in times)
        if total >= n:
            end = mid
        else:
            start = mid + 1
    return start


def solution(n, times):
    answer = binary_search(times, n, 1, max(times) * n)

    return answer

n = 6
times = [7, 10]
# answer = 28
print(solution(n, times))