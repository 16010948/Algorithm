class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, nodes):
        left = None
        if nodes['A']["left"] != '.':
            left = Node(nodes['A']["left"])

        right = None
        if nodes['A']["right"] != '.':
            right = Node(nodes['A']["right"])

        self.root = Node('A', left, right)
        self.build(left, nodes)
        self.build(right, nodes)

    def build(self, cur, nodes):
        if cur == None:
            return
        if nodes[cur.value]["left"] != ".":
            left = Node(nodes[cur.value]["left"])
            cur.left = left
            self.build(left, nodes)
        if nodes[cur.value]["right"] != '.':
            right = Node(nodes[cur.value]["right"])
            cur.right = right
            self.build(cur.right, nodes)

def preorder_traversal(node):
    if node == None:
        return
    print(node.value, end="")
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def inorder_traversal(node):
    if node == None:
        return
    inorder_traversal(node.left)
    print(node.value, end="")
    inorder_traversal(node.right)

def postorder_traversal(node):
    if node == None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.value, end="")

n = int(input())
nodes = {}
for _ in range(n):
    value, left, right = input().split()
    nodes[value] = {
        "left": left,
        "right": right
    }

tree = Tree(nodes)

preorder_traversal(tree.root)
print()
inorder_traversal(tree.root)
print()
postorder_traversal(tree.root)
print()