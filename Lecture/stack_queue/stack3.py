class Multi_Stack:

    class Stack_Info:
        def __init__(self, start, stack_size, outer):
            self.start = start
            self.stack_size = stack_size
            self.data_size = 0
            self.outer = outer


        def is_within_stack(self, index):
            if index < 0 or index >= len(self.outer.values):
                return False
            virtual_index = index + len(self.outer.values) if index < self.start else index
            end = self.start + self.stack_size
            return self.start <= virtual_index and virtual_index < end

        def get_last_stack_index(self):
            return self.outer.adjust_index(self.start + self.stack_size - 1)

        def get_last_data_index(self):
            return self.outer.adjust_index(self.start + self.data_size - 1)

        def get_new_data_index(self):
            return self.outer.adjust_index(self.get_last_data_index() + 1)

        def is_full(self):
            return self.data_size == self.stack_size

        def is_empty(self):
            return self.data_size == 0

    def __init__(self, num_of_stack, default_size):
        self.info = [self.Stack_Info(default_size * i, default_size, self) for i in range(num_of_stack)]
        self.values = [0] * (num_of_stack * default_size)

    def expand(self, stack_num):
        next_stack = (stack_num + 1) % len(self.info)
        self.shift(next_stack)
        self.info[stack_num].stack_size += 1

    def shift(self, stack_num):
        stack = self.info[stack_num]
        if stack.data_size >= stack.stack_size:
            next_stack = (stack_num + 1) % len(self.info)
            self.shift(next_stack)
            stack.stack_size += 1
        index = stack.get_last_data_index()
        while stack.is_within_stack(index):
            self.values = self.values[self.previous_index(index)]
            index = self.previous_index(index)
        self.values[stack.start] = 0
        stack.start = self.next_index(stack.start)
        stack.stack_size -= 1

    def number_of_elements(self):
        total_data_size = 0
        for sd in self.info:
            total_data_size += sd.data_size
        return total_data_size

    def all_stack_are_full(self):
        return self.number_of_elements() == len(self.values)

    def adjust_index(self, index):
        max_index = len(self.values)
        return ((index % max_index) + max_index) % max_index

    def next_index(self, index):
        return self.adjust_index(index + 1)

    def previous_index(self, index):
        return self.adjust_index(index - 1)

    def push(self, stack_num, value):
        if self.all_stack_are_full():
            raise Exception("스택이 가득 찼습니다")
        stack = self.info[stack_num]
        if stack.is_full():
            self.expand(stack_num)
        self.values[stack.get_new_data_index()] = value
        stack.data_size += 1

    def pop(self, stack_num):
        stack = self.info[stack_num]
        if stack.is_empty():
            raise Exception("스택이 비어있습니다")
        last = stack.get_last_data_index()
        value = self.values[last]
        self.values[last] = 0
        stack.data_size -= 1
        return value

    def peek(self, stack_num):
        stack = self.info[stack_num]
        if stack.is_empty():
            raise Exception("스택이 비어있습니다")
        return self.values[stack.get_last_data_index()]

ms = Multi_Stack(3, 5)
try:
    ms.push(0, 1)
    ms.push(0, 2)
    ms.push(0, 3)
    ms.push(0, 4)
    ms.push(0, 5)
    ms.push(0, 6)
    ms.push(0, 7)
    ms.push(0, 8)
    ms.push(0, 9)

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
    print("Stack #0:", ms.pop(0))
    print("Stack #0:", ms.pop(0))
    print("Stack #0:", ms.pop(0))
    print("Stack #0:", ms.pop(0))
    print("Stack #0:", ms.pop(0))
    print("Stack #0:", ms.pop(0))
    print("Stack #0:", ms.pop(0))

    print("Stack #1:", ms.pop(1))
    print("Stack #1:", ms.pop(1))
    print("Stack #1:", ms.peek(1))
    print("Stack #1:", ms.pop(1))
    print("Stack #1:", ms.pop(1))
    print("Stack #1:", ms.pop(1))

except Exception as e:
    print(e)