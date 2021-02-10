class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.below = None
            self.above = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.top = None
        self.bottom = None
        self.size = 0

    def pop(self):
        if self.size == 0:
            raise Exception("스택이 비어있습니다")
        data = self.top.data
        top = self.top.below
        if top == None:
            self.bottom = None
        else:
            top.above = None
        self.size -= 1
        return data

    def pop_bottom(self):
        if self.size == 0:
            raise Exception("스택이 비어있습니다")
        n = self.bottom
        bottom = self.bottom.above
        if bottom == None:
            self.top = None
        else:
            bottom.below = None
        self.size -= 1
        return n

    def push(self, data):
        if self.is_full():
            raise Exception("스택이 가득 찼습니다")
        n = self.Node(data)

        if self.is_empty():
            self.top = n
            self.bottom = n
        else:
            self.top.above = n
            n.below = self.top
            self.top = n
        self.size += 1

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

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
        self.stacks.append(Stack(self.capacity))

    def remove(self, stack_num):
        del self.stacks[stack_num]

    def remove_last_stack(self):
        self.remove(self.size() - 1)

    def push(self, data):
        last = self.get_last_stack()
        if last == None or last.size == self.capacity:
            self.add_stack()
            last = self.get_last_stack()
        try:
           last.push(data)
        except Exception as e:
            print(e)

    def pop(self):
        last = self.get_last_stack()
        if last == None or last.is_empty():
            raise Exception("스택이 비어있습니다")
        data = last.pop()
        if last.is_empty():
            self.remove_last_stack()
        return data

    def pop_at(self, index):
        if self.size() <= 0:
            raise Exception("스택이 비어있습니다")
        if index < 0 or index >= self.size():
            raise Exception("범위를 초과하였습니다")
        stack = self.get(index)
        if stack == None or stack.is_empty():
            raise Exception("스택이 비어있습니다")
        data = stack.pop()
        self.shift_left(index)
        return data

    def shift_left(self, index):
        if index < self.size() - 1:
            right = self.get(index + 1)
            left = self.get(index)
            try:
                left.push(right.pop_bottom())
            except Exception as e:
                print(e)
            if right.is_empty():
                self.remove(index + 1)
            self.shift_left(index + 1)

sos = Set_of_Stacks(3)
sos.push(1)
sos.push(2)
sos.push(3)

sos.push(4)
sos.push(5)
sos.push(6)

sos.push(7)
sos.push(8)

print(sos.pop_at(0))    # 3
print(sos.pop_at(1))    # 7
