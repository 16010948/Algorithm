import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

jewelry = []
for _ in range(n):
    weight, value = map(int, input().split())
    heapq.heappush(jewelry, [weight, value])

bag = []
for _ in range(k):
    capacity = int(input())
    heapq.heappush(bag, capacity)

total = 0
for _ in range(k):
    capacity = heapq.heappop(bag)

    weight, value = heapq.heappop(jewelry)
    if weight > capacity:
        heapq.heappush(jewelry, [weight, value])
        continue

    total += value

    if not jewelry:
        break

print(total)