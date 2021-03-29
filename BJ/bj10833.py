n = int(input())

answer = 0
for _ in range(n):
    student, apple = map(int, input().split())
    answer += apple % student
print(answer)