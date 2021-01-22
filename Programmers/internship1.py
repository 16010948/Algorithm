class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def put(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data) - 1]

    def size(self):
        return len(self.data)


def solution(board, moves):
    answer = 0
    stack = Stack()

    for x in moves:
        for b in board:
            if b[x - 1] != 0:
                if not stack.is_empty() and stack.peek() == b[x - 1]:
                    answer += 2
                    stack.pop()
                else:
                    stack.put(b[x - 1])
                b[x - 1] = 0
                break

    return answer

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
# answer = 4
print(solution(board, moves))