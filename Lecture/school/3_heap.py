class Heap:
    def __init__(self):
        self.array = [0] * 100
        self.n = 0

    def up_heap(self, i):
        if i // 2 == 0:
            return

        if self.array[i] > self.array[i // 2]:
            self.array[i], self.array[i // 2] = self.array[i // 2], self.array[i]
            self.up_heap(i // 2)

    def down_heap(self, i):
        bg = i * 2 if self.array[i * 2] > self.array[i * 2 + 1] else i * 2 + 1
        if self.array[bg] == 0:
            return
        if self.array[bg] > self.array[i]:
            self.array[bg], self.array[i] = self.array[i], self.array[bg]
            self.down_heap(bg)


    def insert_item(self, key):
        self.n += 1
        self.array[self.n] = key
        self.up_heap(self.n)
        return 0

    def remove_max(self):
        key = self.array[1]
        self.array[1] = self.array[self.n]
        self.n -= 1
        self.down_heap(1)
        return key

    def print_heap(self):
        for i in range(1, self.n + 1):
            print(self.array[i], end=" ")
        print()

    def r_build_heap(self, i):
        if i > self.n:
            return
        self.r_build_heap(2 * i)
        self.r_build_heap(2 * i + 1)
        self.down_heap(i)

    def build_heap(self):
        for i in range(self.n // 2, 0, -1):
            self.down_heap(i)

heap = Heap()
'''
while True:
    command = input().split()
    if command[0] == 'q':
        break
    elif command[0] == 'i':
        success_value = heap.insert_item(int(command[1]))
        print(success_value)
    elif command[0] == 'd':
        max_value = heap.remove_max()
        print(max_value)
    elif command[0] == 'p':
        heap.print_heap()
'''
n = int(input())
array = list(map(int, input().split()))
heap.n = n
for i in range(1, n + 1):
    heap.array[i] = array[i - 1]
heap.r_build_heap(1)
heap.print_heap()