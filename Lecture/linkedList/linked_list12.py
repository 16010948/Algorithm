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
def reverse_and_clone(node):
    head = None
    while node != None:
        n = Node(node.data)
        n.next = head
        head = n
        node = node.next
    return head

def is_equal(l1, l2):
    while l1 != None and l2 != None:
        if l1.data != l2.data:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 == None and l2 == None

def is_palindrome(head):
    reversed = reverse_and_clone(head)
    return is_equal(head, reversed)

l1 = LinkedList()
l1.append('m')
l1.append('a')
l1.append('d')
l1.append('a')
l1.append('m')
l1.retrieve()
print(is_palindrome(l1.get(1)))

l2 = LinkedList()
l2.append('l')
l2.append('i')
l2.append('e')
l2.retrieve()
print(is_palindrome(l2.get(1)))

