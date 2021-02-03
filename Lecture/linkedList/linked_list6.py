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

    def size(self):
        n = self.header
        total = 1
        while n.next != None:
            total += 1
            n = n.next
        return total

def kth_to_last(n, k):
    p1 = n.header
    for _ in range(k):
        if p1 == None:
            return None
        p1 = p1.next
    p2 = n.header
    while p1 != None:
        p1 = p1.next
        p2 = p2.next
    return p2

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.retrieve()
k = 3
found = kth_to_last(ll, k)
print("last k(", k, ")th data is", found.data)