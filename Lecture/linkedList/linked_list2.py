class Node:
    def __init__(self):
        self.data = None
        self.next = None

class linked_list:
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

ll = linked_list()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.retrieve()
ll.delete(1)
ll.retrieve()