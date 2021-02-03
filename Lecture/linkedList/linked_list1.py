class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def append(self, d):
        end = Node(d)
        n = self
        while n.next != None:
            n = n.next
        n.next = end

    def delete(self, d):
        n = self
        while n.next != None:
            if n.next.data == d:
                n.next = n.next.next
            else:
                n = n.next

    def retrieve(self):
        n = self
        while n.next != None:
            print(n.data, end=" -> ")
            n = n.next
        print(n.data)

head = Node(1)
head.append(2)
head.append(3)
head.append(4)
head.retrieve()
head.delete(2)
head.delete(3)
head.retrieve()