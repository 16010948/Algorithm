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

    def size(self):
        n = self.header
        total = 0
        while n.next != None:
            total += 1
            n = n.next
        return total

def get_intersection(l1, l2):
    size1 = l1.size()
    size2 = l2.size()

    if size1 > size2:
        l1 = l1.get(size1 - size2)
        l2 = l2.header
    elif size2 > size1:
        l2 = l2. get(size2 - size1)
        l1 = l1.header

    while l1 != None and l2 != None:
        if l1.data == l2.data:
            return l1
        l1 = l1.next
        l2 = l2.next

    return None


l1 = LinkedList()
l1.append(5)
l1.append(7)
l1.append(9)
l1.append(10)
l1.append(7)
l1.append(6)
l1.retrieve()

l2 = LinkedList()
l2.append(1)
l2.append(2)
l2.append(3)
l2.append(4)
l2.append(5)
l2.retrieve()

n = get_intersection(l1, l2)
if n != None:
    print("Intersection:", n.data)
else:
    print("Not found")

