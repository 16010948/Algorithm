class Queue:
    class Node:
        def __init__(self, data):
            self.data = data;
            self.next = None;

    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        t = self.Node(item)

        if self.last != None:
            self.last.next = t
        self.last = t

        if self.first == None:
            self.first = self.last

    def remove(self):
        if self.first == None:
            raise Exception("큐가 비어있습니다")
        data = self.first.data
        self.first = self.first.next

        if self.first == None:
            self.last = None
        return data

    def peek(self):
        if self.first == None:
            raise Exception("큐가 비어있습니다")
        return self.first.data

    def is_empty(self):
        return self.first == None

q = Queue()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
print(q.remove())
print(q.remove())
print(q.peek())
print(q.remove())
print(q.is_empty())
print(q.remove())
print(q.is_empty())