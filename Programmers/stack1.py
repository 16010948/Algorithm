class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, value):
        self.data.append(value)

    def peek(self):
        return self.data[len(self.data) - 1]

    def pop(self):
        return self.data.pop()


class Stock:
    def __init__(self, index, price):
        self.index = index
        self.price = price


def solution(prices):
    answer = [0] * len(prices)
    stack = Stack()

    for i, price in enumerate(prices):
        while not stack.is_empty():
            if stack.peek().price > price:
                tmp = stack.pop()
                answer[tmp.index] = i - tmp.index
            else:
                break
        stack.push(Stock(i, price))

    l = len(answer) - 1
    for i in range(l):
        if answer[i] == 0:
            answer[i] = l - i
    return answer

prices = [1, 2, 3, 2, 3]
# answer = [4, 3, 1, 1, 0]
print(solution(prices))