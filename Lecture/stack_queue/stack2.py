class Fixed_Multi_Stack:
    NUM_OF_STACK = 3
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.sizes = [0] * self.NUM_OF_STACK
        self.values = [0] * self.NUM_OF_STACK * stack_size

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.stack_size == self.sizes[stack_num]

    def get_top_index(self, stack_num):
        offset = self.stack_size * stack_num
        size = self.sizes[stack_num]
        return offset + size - 1

    def push(self, stack_num, data):
        if self.is_full(stack_num):
            raise Exception("스택이 가득 찼습니다")
        self.values[self.get_top_index(stack_num) + 1] = data
        self.sizes[stack_num] += 1

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("스택이 비어 있습니다")
        top = self.get_top_index(stack_num)
        data = self.values[top]
        self.values[top] = 0
        self.sizes[stack_num] -= 1
        return data

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("스택이 비어 있습니다")
        return self.values[self.get_top_index(stack_num)]

ms = Fixed_Multi_Stack(5)
try:
    ms.push(0, 1)
    ms.push(0, 2)
    ms.push(0, 3)
    ms.push(0, 4)
    ms.push(0, 5)
    ms.push(0, 6)

    ms.push(1, 11)
    ms.push(1, 12)
    ms.push(1, 13)
    ms.push(1, 14)
    ms.push(1, 15)

except Exception as e:
    print(e)

try:
    print("Stack #0:", ms.pop(0))
    print("Stack #0:", ms.pop(0))
    print("Stack #0:", ms.peek(0))
    print("Stack #0:", ms.pop(0))
    print("Stack #0:", ms.is_empty(0))
    print("Stack #0:", ms.pop(0))
    print("Stack #0:", ms.pop(0))
    print("Stack #0:", ms.is_empty(0))

    print("Stack #1:", ms.pop(1))
    print("Stack #1:", ms.pop(1))
    print("Stack #1:", ms.peek(1))
    print("Stack #1:", ms.pop(1))
    print("Stack #1:", ms.is_empty(1))
    print("Stack #1:", ms.pop(1))
    print("Stack #1:", ms.pop(1))
    print("Stack #1:", ms.is_empty(1))

except Exception as e:
    print(e)