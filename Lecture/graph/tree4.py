class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def make_tree(self, a):
        self.root = self.make_tree_recursive(a, 0, len(a) - 1)

    def make_tree_recursive(self, a, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = self.Node(a[mid])
        node.left = self.make_tree_recursive(a, start, mid - 1)
        node.right = self.make_tree_recursive(a, mid + 1, end)
        return node

    def search_binary_tree(self, n, find):
        if find < n.data:
            print("data is smaller than", n.data)
            self.search_binary_tree(n.left, find)
        elif find > n.data:
            print("data is bigger than", n.data)
            self.search_binary_tree(n.right, find)
        else:
            print("Data found!")

a = []
for i in range(10):
    a.append(i)

t = Tree()
t.make_tree(a)
t.search_binary_tree(t.root, 2)