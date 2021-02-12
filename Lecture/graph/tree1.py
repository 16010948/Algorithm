class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, node):
        self.root = node

    def get_root(self):
        return self.root

    def make_node(self, data, left, right):
        node = Node(data, left, right)
        return node

    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print("inorder:", node.data)
            self.inorder(node.right)

    def preorder(self, node):
        if node != None:
            print("preorder:", node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print("postorder:", node.data)

t = Tree()
n4 = t.make_node(4, None, None)
n5 = t.make_node(5, None, None)
n2 = t.make_node(2, n4, n5)
n3 = t.make_node(3, None, None)
n1 = t.make_node(1, n2, n3)
t.set_root(n1)
t.inorder(t.get_root())
t.preorder(t.get_root())
t.postorder(t.get_root())

