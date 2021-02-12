class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self, size):
        self.root = self.make_BST(0, size - 1)

    def make_BST(self, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = self.Node(mid)
        node.left = self.make_BST(start, mid - 1)
        node.right = self.make_BST(mid + 1, end)
        return node

    def BST_to_list(self):
        lists = []
        self.BST_to_list_recursive(self.root, lists, 0)
        return lists

    def BST_to_list_recursive(self, root, lists, level):
        if root == None:
            return
        level_list = []
        if len(lists) == level:
            lists.append(level_list)
        else:
            level_list = lists[level]
        level_list.append(root)
        self.BST_to_list_recursive(root.left, lists, level + 1)
        self.BST_to_list_recursive(root.right, lists, level + 1)

    def BST_to_lists2(self):
        result = []
        current = []
        if self.root != None:
            current.append(self.root)
        while len(current) > 0:
            result.append(current)
            parents = current
            current = []
            for parent in parents:
                if parent.left != None:
                    current.append(parent.left)
                if parent.right != None:
                    current.append(parent.right)
        return result

    def print_list(self, arr):
        for list in arr:
            for node in list:
                print(node.data, end=" ")
            print()

t = Tree(10)
# t.print_list(t.BST_to_list())
t.print_list(t.BST_to_lists2())
