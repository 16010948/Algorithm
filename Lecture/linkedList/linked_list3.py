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

    def remove_dups(self):
        n = self.header
        while n != None and n.next != None:
            r = n
            while r.next != None:
                if n.data == r.next.data:
                    r.next = r.next.next
                else:
                    r = r.next
            n = n.next

ll = LinkedList()
ll.append(2)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(4)
ll.append(2)
ll.retrieve()
ll.remove_dups()
ll.retrieve()