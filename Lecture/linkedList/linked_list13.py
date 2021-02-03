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
class Storage:
    def __init__(self, n, r):
        self.node = n
        self.result = r

def is_palindrome_recursive(head, length):
    if head == None or length <= 0:
        return Storage(head, True)
    elif length == 1:
        return Storage(head.next, True)
    storage = is_palindrome_recursive(head.next, length -2)
    if not storage.result or storage.node == None:
        return storage
    storage.result = (head.data == storage.node.data)
    storage.node = storage.node.next
    return storage

def is_palindrome(head, size):
    storage = is_palindrome_recursive(head, size)
    return storage.result

l1 = LinkedList()
l1.append('m')
l1.append('a')
l1.append('d')
l1.append('a')
l1.append('m')
l1.retrieve()
print(is_palindrome(l1.get(1), l1.size()))

l2 = LinkedList()
l2.append('l')
l2.append('i')
l2.append('e')
l2.append('e')
l2.retrieve()
print(is_palindrome(l2.get(1), l2.size()))

