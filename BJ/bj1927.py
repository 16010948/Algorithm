import sys
input = sys.stdin.readline

class MinHeap:
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
            if self.queue[index] < self.queue[parent_index]:
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
        min_value = self.queue.pop()
        self.min_heapify(1)
        return min_value

    def min_heapify(self, index):
        last_index = self.length()
        left_index = self.left_child(index)
        right_index = self.right_child(index)

        min_index = index

        if left_index <= last_index and self.queue[min_index] > self.queue[left_index]:
            min_index = left_index
        if right_index <= last_index and self.queue[min_index] > self.queue[right_index]:
            min_index = right_index

        if min_index != index:
            self.swap(index, min_index)
            self.min_heapify(min_index)

    def print_heap(self):
        print(self.queue)

n = int(input())

heap = MinHeap()
for _ in range(n):
    element = int(input())
    if element == 0:
        min_value = heap.delete()
        print(min_value)
    else:
        heap.insert(element)