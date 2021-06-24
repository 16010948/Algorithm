class Tree:
    class Node:
        def __init__(self, data):
            self.data = data

    def __init__(self):
        self.root = None
        self.p_index = 0

    def build_tree_by_in_pre(self, in_o, pre_o):
        self.p_index = 0
        self.root = self.build_tree_by_in_pre_recursive(in_o, pre_o, 0, len(in_o) - 1)

    def build_tree_by_in_pre_recursive(self, in_o, pre_o, start, end):
        if start > end:
            return None
        node = self.Node(pre_o[self.p_index])
        self.p_index += 1
        if start == end:
            return node
        mid = self.search(in_o, start, end, node.data)
        node.left = self.build_tree_by_in_pre_recursive(in_o, pre_o, start, mid - 1)
        node.right = self.build_tree_by_in_pre_recursive(in_o, pre_o, mid + 1, end)
        return node

    def build_tree_by_in_post(self, in_o, post_o):
        self.p_index = len(post_o) - 1
        self.root = self.build_tree_by_in_post_recursive(in_o, post_o, 0, len(in_o) - 1)

    def build_tree_by_in_post_recursive(self, in_o, post_o, start, end):
        if start > end:
            return None
        node = self.Node(post_o[self.p_index])
        self.p_index -= 1
        if start == end:
            return node
        mid = self.search(in_o, start, end, node.data)
        node.right = self.build_tree_by_in_post_recursive(in_o, post_o, mid + 1, end)
        node.left = self.build_tree_by_in_post_recursive(in_o, post_o, start, mid - 1)
        return node

    def search(self, arr, start, end, value):
        for i in range(start, end + 1):
            if arr[i] == value:
                return i
        return end + 1

    def print_inorder(self, node):
        if node == None:
            return
        self.print_inorder(node.left)
        print(node.data, end=" ")
        self.print_inorder(node.right)

tree = Tree()
pre_o = [4, 2, 1, 3, 6, 5, 7]
in_o = [1, 2, 3, 4, 5, 6, 7]
post_o = [1, 3, 2, 5, 7, 6, 4]

tree.build_tree_by_in_post(in_o, pre_o)
tree.print_inorder(tree.root)
