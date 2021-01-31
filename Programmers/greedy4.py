def solution(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
        right -= 1

    return len(people) - answer

people = [70, 50, 80, 50]
limit = 100
# answer = 3
print(solution(people, limit))

people = [70, 80, 50]
limit = 100
# answer = 3
print(solution(people, limit))

