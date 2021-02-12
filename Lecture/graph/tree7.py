MIN_INF = int(-1e9)

class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None


    def __init__(self, size):
        self.root = self.make_BST(0, size - 1)
        # self.root.right.right.right.right = self.Node(10)

    def make_BST(self, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = self.Node(mid)
        node.left = self.make_BST(start, mid - 1)
        node.right = self.make_BST(mid + 1, end)
        return node

    def is_balanced(self, root):
        if root == None:
            return True
        height_diff = abs(self.get_height(root.left) - self.get_height(root.right))
        if height_diff > 1:
            return False
        else:
            return self.is_balanced(root.left) and self.is_balanced(root.right)


    def get_height(self, root):
        if root == None:
            return -1
        return max(self.get_height(root.left), self.get_height(root.right)) + 1

    def check_height(self, root):
        if root == None:
            return -1
        left_height = self.check_height(root.left)
        if left_height == MIN_INF:
            return MIN_INF
        right_height = self.check_height(root.right)
        if right_height == MIN_INF:
            return MIN_INF
        height_diff = abs(left_height - right_height)

        if height_diff > 1:
            return MIN_INF
        else:
            return max(left_height, right_height) + 1

    def is_balanced2(self, root):
        return self.check_height(root) != MIN_INF


t = Tree(10)
print(t.is_balanced2(t.root))