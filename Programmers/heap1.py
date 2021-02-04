import heapq


def solution(scoville, K):
    answer = 0
    q = []

    for value in scoville:
        heapq.heappush(q, value)

    while q[0] < K:
        s1 = heapq.heappop(q)
        s2 = heapq.heappop(q)
        heapq.heappush(q, s1 + (s2 * 2))
        answer += 1
        if len(q) == 1 and q[0] < K:
            answer = -1
            break

    return answer

scoville = [1, 2, 3, 9, 10, 12]
k = 7
# answer = 2
print(solution(scoville, k))