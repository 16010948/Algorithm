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

def size(l):
    total = 0
    while l != None:
        total += 1
        l = l.next
    return total

class Storage:
    def __init__(self):
        self.carry = 0
        self.result = None

def insert(n, data):
    before = Node()
    before.data = data
    if n != None:
        before.next = n
    return before

def l_pad_list(l, length):
    head = l
    for _ in range(length):
        head = insert(head, 0)
    return head

def add_list(l1, l2):
    if l1 == None and l2 == None:
        storage = Storage()
        return storage
    storage = add_list(l1.next, l2.next)
    value = storage.carry + l1.data + l2. data
    data = value % 10
    storage.result = insert(storage.result, data)
    storage.carry = value // 10
    return storage

def sum_list(l1, l2):
    len1 = size(l1)
    len2 = size(l2)

    if len1 > len2:
        l2 = l_pad_list(l2, len1 - len2)
    else:
        l1 = l_pad_list(l1, len2 - len1)
    storage = add_list(l1, l2)
    if storage.carry != 0:
        storage.result = insert(storage.result, storage.carry)
    return storage.result

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

n1 = sum_list(l1.get(1), l2.get(1))
while n1 != None:
    print(n1.data)
    n1 = n1.next

l3 = LinkedList()
l3.append(9)
l3.append(1)
l3.retrieve()

l4 = LinkedList()
l4.append(1)
l4.retrieve()

n2 = sum_list(l3.get(1), l4.get(1))
while n2 != None:
    print(n2.data)
    n2 = n2.next

