class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.header = Node(None)

    def append(self, d):
        end = Node(d)
        n = self.header
        while n.next != None:
            n = n.next
        n.next = end

    def delete(self, d):
        n = self.header
        while n.next != None:
            if n.next.data == d:
                n.next = n.next.next
            else:
                n = n.next

    def retrieve(self):
        n = self.header.next
        while n.next != None:
            print(n.data, end=" -> ")
            n = n.next
        print(n.data)

    def get(self, k):
        n = self.header
        for _ in range(k):
            if n == None:
                return None
            n = n.next
        return n

def partition(n, x):
    s1 = Node(None)
    e1 = Node(None)
    s2 = Node(None)
    e2 = Node(None)
    while n != None:
        next = n.next
        n.next = None
        if n.data < x:
            if s1.data == None:
                s1 = n
                e1 = s1
            else:
                e1.next = n
                e1 = n
        else:
            if s2.data == None:
                s2 = n
                e2 = s2
            else:
                e2.next = n
                e2 = n
        n = next
    if s1 == None:
        return s2
    e1.next = s2
    return s1

ll = LinkedList()
ll.append(7)
ll.append(2)
ll.append(8)
ll.append(5)
ll.append(3)
ll.append(4)
ll.retrieve()
n = partition(ll.get(1), 5)
while n.next != None:
    print(n.data, end=" -> ")
    n = n.next
print(n.data)