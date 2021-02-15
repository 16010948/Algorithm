MIN_VALUE = int(-1e9)
MAX_VALUE = int(1e9)

class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self, size):
        self.size = size
        self.root = self.make_BST(0, size - 1)

    def make_BST(self, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = self.Node(mid)
        node.left = self.make_BST(start, mid - 1)
        node.right = self.make_BST(mid + 1, end)
        return node

    def is_validate_BST1(self):
        array = [0] * self.size
        self.inorder(self.root, array)
        for i in range(self.size):
            if array[i].data < array[i - 1].data:
                return False
        return True
    index = 0
    def inorder(self, root, array):
        if root != None:
            self.inorder(root.left, array)
            array[self.index] = self.root
            self.index += 1
            self.inorder(root.right, array)

    last_printed = None
    def is_validate_BST2(self, n):
        if n == None:
            return True
        if not self.is_validate_BST2(n.left):
            return False
        if self.last_printed != None and n.data < self.last_printed:
            return False
        self.last_printed = n.data
        if not self.is_validate_BST2(n.right):
            return False
        return True

    def is_validate_BST3(self, n, min_value, max_value):
        if n == None:
            return True
        if n.data < min_value or n.data > max_value:
            return False
        if not self.is_validate_BST3(n.left, min_value, n.data) or not self.is_validate_BST3(n.right, n.data, max_value):
            return False


t = Tree(10)
print("solution1: using inorder", t.is_validate_BST1())
print("solution1: without array", t.is_validate_BST2(t.root))
print("solution1: without array", t.is_validate_BST3(t.root, MIN_VALUE, MAX_VALUE))