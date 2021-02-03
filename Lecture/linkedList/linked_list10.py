class Node:
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.header = Node()

    def append(self, d):
        end = Node()
        end.data = d
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
def sum_list(l1, l2, carry):
    if l1 == None and l2 == None and carry == 0:
        return None
    result = Node()
    value = carry
    if l1 != None:
        value += l1.data
    if l2 != None:
        value += l2.data
    result.data = value % 10
    if l1 != None or l2 != None:
        next = sum_list(l1.next if l1 != None else None,
                        l2.next if l2 != None else None,
                        value // 10)
        result.next = next
    return result

l1 = LinkedList()
l1.append(9)
l1.append(1)
l1.append(4)
l1.retrieve()

l2 = LinkedList()
l2.append(6)
l2.append(4)
l2.append(3)
l2.retrieve()

n1 = sum_list(l1.get(1), l2.get(1), 0)
while n1 != None:
    print(n1.data)
    n1 = n1.next

l3 = LinkedList()
l3.append(1)
l3.retrieve()

l4 = LinkedList()
l4.append(9)
l4.append(9)
l4.retrieve()

n2 = sum_list(l3.get(1), l4.get(1), 0)
while n2 != None:
    print(n2.data)
    n2 = n2.next

