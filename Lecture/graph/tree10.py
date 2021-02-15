class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self, size):
        self.root = self.make_BST(0, size - 1, None)

    def make_BST(self, start, end, parent):
        if start > end:
            return None
        mid = (start + end) // 2
        node = self.Node(mid)
        node.left = self.make_BST(start, mid - 1, node)
        node.right = self.make_BST(mid + 1, end, node)
        node.parent = parent

        return node

    def find_next(self, node):
        if node.right == None:
            print(self.find_above(node.parent, node).data, "is", node.data, "'s next")
        else:
            print(self.find_below(node.right).data, "is", node.data, "'s next")

    def find_above(self, root, child):
        if root == None:
            return None
        if root.left == child:
            return root
        return self.find_above(root.parent, root)

    def find_below(self, root):
        if root.left == None:
            return root
        return self.find_below(root.left)

t = Tree(10)
t.find_next(t.root.left.right.right)
t.find_next(t.root.left)
t.find_next(t.root)
t.find_next(t.root.left.left)
t.find_next(t.root.right.left.right)