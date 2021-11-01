import sys
input = sys.stdin.readline

class MaxHeap:
    def __init__(self):
        self.queue = [0]

    def parent(self, index):
        return index // 2

    def left_child(self, index):
        return index * 2

    def right_child(self, index):
        return index * 2 + 1

    def swap(self, index, parent_index):
        self.queue[index], self.queue[parent_index] = self.queue[parent_index], self.queue[index]

    def insert(self, n):
        self.queue.append(n)

        index = self.length()
        while index > 1:
            parent_index = self.parent(index)
            if self.queue[index] > self.queue[parent_index]:
                self.swap(index, parent_index)
                index = parent_index
            else:
                break

    def length(self):
        return len(self.queue) - 1

    def delete(self):
        last_index = self.length()
        if last_index == 0:
            return 0

        self.swap(1, last_index)
        max_value = self.queue.pop()
        self.max_heapify(1)
        return max_value

    def max_heapify(self, index):
        last_index = self.length()
        left_index = self.left_child(index)
        right_index = self.right_child(index)

        max_index = index

        if left_index <= last_index and self.queue[max_index] < self.queue[left_index]:
            max_index = left_index
        if right_index <= last_index and self.queue[max_index] < self.queue[right_index]:
            max_index = right_index

        if max_index != index:
            self.swap(index, max_index)
            self.max_heapify(max_index)

    def print_heap(self):
        print(self.queue)

n = int(input())

heap = MaxHeap()
for _ in range(n):
    element = int(input())
    if element == 0:
        max_value = heap.delete()
        print(max_value)
    else:
        heap.insert(element)