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

def delete_node(n):
    if n == None or n.next == None:
        return False
    next = n.next
    n.data = next.data
    n.next = next.next
    next.next = None
    return True

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.retrieve()
delete_node(ll.get(3))
ll.retrieve()