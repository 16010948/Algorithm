class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def add_next(self, d):
        if type(d) == int:
            end = Node(d)
            self.next = end
            return end
        else:
            self.next = d

    def print(self):
        n = self
        while n.next != None:
            print(n.data, end=" -> ")
            n = n.next
        print(n.data)

    def size(self):
        n = self
        total = 0
        while n != None:
            total += 1
            n = n.next
        return total

    def get(self, k):
        n = self
        for _ in range(k):
            n = n.next
        return n

def get_intersection(n1, n2):
    size1 = n1.size()
    size2 = n2.size()

    if size1 > size2:
        n1 = n1.get(size1 - size2)
    elif size2 > size1:
        n2 = n2. get(size2 - size1)

    while n1 != None and n2 != None:
        if n1 == n2:
            return n1
        n1 = n1.next
        n2 = n2.next

    return None


n1 = Node(5)
n2 = n1.add_next(7)
n3 = n2.add_next(9)
n4 = n3.add_next(10)
n5 = n4.add_next(7)
n6 = n5.add_next(6)
n1.print()

m1 = Node(6)
m2 = m1.add_next(8)
m2.add_next(n4)
m1.print()

n = get_intersection(n1, m1)
if n != None:
    print("Intersection:", n.data)
else:
    print("Not found")

