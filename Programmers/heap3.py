class Heap:
    def __init__(self):
        self.queue = []

    def insert(self, n):
        start = 0
        end = len(self.queue)
        mid = (start + end) // 2
        while start < end:
            if self.queue[mid] < n:
                start = mid + 1
            elif self.queue[mid] > n:
                end = mid
            else:
                break
            mid = (start + end) // 2

        index = max(mid, 0)
        self.queue.insert(index, n)

    def is_empty(self):
        return len(self.queue) <= 0

    def pop(self, value):
        if self.is_empty():
            return

        if value > 0:
            self.queue.pop()
        else:
            self.queue.pop(0)


def solution(operations):
    answer = [0, 0]
    heap = Heap()
    for operation in operations:
        op, value = operation.split()
        if op == 'I':
            heap.insert(int(value))
        elif op == 'D':
            heap.pop(int(value))
    if not heap.is_empty():
        answer[0] = heap.queue[-1]
        answer[1] = heap.queue[0]
    return answer

operations = ["I 16", "D 1"]
# answer = [0, 0]
print(solution(operations))

operations = ["I 7", "I 5", "I -5", "D -1"]
# answer = [7, 5]
print(solution(operations))