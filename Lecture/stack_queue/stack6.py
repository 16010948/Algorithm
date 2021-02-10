class Stack:

    def __init__(self):
        self.data = []

    def pop(self):
        if self.size() == 0:
            raise Exception("스택이 비어있습니다")
        return self.data.pop()

    def push(self, item):
        self.data.append(item)

    def peek(self):
        if self.size() == 0:
            raise Exception("스택이 비어있습니다")
        return self.data[-1]

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

class Set_of_Stacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def size(self):
        return len(self.stacks)

    def get(self, stack_num):
        return self.stacks[stack_num]

    def get_last_stack(self):
        if self.size() == 0:
            return None
        return self.get(self.size() - 1)

    def add_stack(self):
        self.stacks.append(Stack())

    def remove(self, stack_num):
        del self.stacks[stack_num]

    def remove_last_stack(self):
        self.remove(self.size() - 1)

    def push(self, data):
        last = self.get_last_stack()
        if last == None or last.size() == self.capacity:
            self.add_stack()
            last = self.get_last_stack()
        last.push(data)

    def pop(self):
        last = self.get_last_stack()
        if last == None or last.is_empty():
            raise Exception("스택이 비어있습니다")
        data = last.pop()
        if last.is_empty():
            self.remove_last_stack()
        return data

sos = Set_of_Stacks(3)
sos.push(1)
sos.push(2)
sos.push(3)

sos.push(4)
sos.push(5)
sos.push(6)

sos.push(7)
sos.push(8)

print(sos.pop())
print(sos.pop())
print(sos.pop())
print(sos.pop())
