class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def make_BST(self, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = self.Node(mid)
        node.left = self.make_BST(start, mid - 1)
        node.right = self.make_BST(mid + 1, end)
        return node

    def contains_tree(self, t1, t2):
        if t2 == None:
            return True
        return self.sub_tree(t1, t2)

    def sub_tree(self, t1, t2):
        if t1 == None:
            return False
        elif t1.data == t2.data and self.match_tree(t1, t2):
            return True
        return self.sub_tree(t1.left, t2) or self.sub_tree(t1.right, t2)

    def match_tree(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        elif t1 == None or t2 == None:
            return False
        elif t1.data != t2.data:
            return False
        else:
            return self.match_tree(t1.left, t2.left) and self.match_tree(t1.right, t2.right)

t1 = Tree()
t2 = Tree()
t1.root = t1.make_BST(0, 9)
t2.root = t2.make_BST(5, 9)
result = t1.contains_tree(t1.root, t2.root)
print(result)

t3 = Tree()
t3.root = t3.make_BST(7, 9)
result2 = t1.contains_tree(t1.root, t3.root)
print(result2)
