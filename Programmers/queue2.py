from queue import PriorityQueue

def solution(priorities, location):
    answer = 0
    queue = PriorityQueue()
    for priority in priorities:
        queue.put(priority * (-1))

    i = 0
    while not queue.empty():
        answer += 1
        priority = queue.get() * (-1)
        for j in range(len(priorities)):
            index = (i + j) % len(priorities)
            if priorities[index] == priority:
                if index == location:
                    return answer
                i = index + 1
                break

priorities = [2, 1, 3, 2]
location = 2
# answer = 1
print(solution(priorities, location))

priorities = [1, 1, 9, 1, 1, 1]
location = 0
# answer = 5
print(solution(priorities, location))