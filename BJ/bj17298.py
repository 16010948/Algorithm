import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [-1 for _ in range(n)]
for i in range(n):
    while len(stack) > 0 and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

for a in answer:
    print(a, end=" ")