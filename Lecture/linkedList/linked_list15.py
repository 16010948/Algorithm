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

def find_loop(head):
    fast = head
    slow = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            break

    if fast == None or fast.next == None:
        return None

    slow = head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    return fast

n1 = Node(1)
n2 = n1.add_next(2)
n3 = n2.add_next(3)
n4 = n3.add_next(4)
n5 = n4.add_next(5)
n6 = n5.add_next(6)
n7 = n6.add_next(7)
n8 = n7.add_next(8)
n8.add_next(n4)

n = find_loop(n1)
if n != None:
   print("start of loop:", n.data)
else:
    print("loop not found")