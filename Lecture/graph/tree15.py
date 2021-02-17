import random

class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.size = 1

        def get_size(self):
            return self.size

        def find(self, data):
            if data == self.data:
                return self
            elif data < self.data:
                return self.left.find(data) if self.left != None else None
            elif data > self.data:
                return self.right.find(data) if self.right != None else None
            else:
                return None

        def get_nth_node(self, n):
            left_size = 0 if self.left == None else self.left.get_size()
            if n < left_size:
                return self.left.get_nth_node(n)
            elif n == left_size:
                return self
            else:
                return self.right.get_nth_node(n - (left_size + 1))

    def __init__(self):
        self.root = None

    def size(self):
        return 0 if self.root == None else self.root.get_size()

    def insert(self, data):
        if self.root == None:
            self.root = self.Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data <= node.data:
            if node.left == None:
               node.left = self.Node(data)
            else:
                self.insert_node(data, node.left)
        else:
            if node.right == None:
                node.right = self.Node(data)
            else:
                self.insert_node(data, node.right)
        node.size += 1


    def get_random_node(self):
        if self.root == None:
            return None
        i = random.randint(0, self.size())
        return self.root.get_nth_node(i)

t = Tree()
t.insert(4)
t.insert(0)
t.insert(1)
t.insert(2)
t.insert(5)
t.insert(7)
t.insert(8)
t.insert(3)
t.insert(6)
t.insert(9)
print(t.get_random_node().data)