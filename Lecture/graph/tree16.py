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

    def count_paths_with_sum(self, root, target):
        if root == None:
            return 0
        paths_from_root = self.count_paths_with_sum_from_node(root, target, 0)
        paths_on_left = self.count_paths_with_sum(root.left, target)
        paths_on_right = self.count_paths_with_sum(root.right, target)
        return paths_from_root + paths_on_left + paths_on_right

    def count_paths_with_sum_from_node(self, node, target, current):
        if node == None:
            return 0
        current += node.data
        total_paths = 0
        if current == target:
            total_paths += 1
        total_paths += self.count_paths_with_sum_from_node(node.left, target, current)
        total_paths += self.count_paths_with_sum_from_node(node.right, target, current)

        return total_paths

    def count_paths_with_sum2(self, target):
        array = []
        return self.count_paths_with_sum_and_array(self.root, target, array)

    def count_paths_with_sum_and_array(self, root, target, array):
        if root == None:
            return 0
        self.add_value(array, root.data)
        total_paths = self.count_paths(array, target)
        total_paths += self.count_paths_with_sum_and_array(root.left, target, array)
        total_paths += self.count_paths_with_sum_and_array(root.right, target, array)
        self.remove_last(array)
        return total_paths

    def add_value(self, array, value):
        for i in range(len(array)):
            array[i] += value
        array.append(value)

    def count_paths(self, array, target):
        total_paths = 0
        for i in range(len(array)):
            if target == array[i]:
                total_paths += 1
        return total_paths

    def remove_last(self, array):
        value = array.pop()
        for i in range(len(array)):
            array[i] -= value

    def count_paths_with_sum3(self, target):
        hash_table = {}
        hash_table[0] = 1
        return self.count_paths_with_sum_and_hash(self.root, target, 0, hash_table)

    def count_paths_with_sum_and_hash(self, node, target, current, hash_table):
        if node == None:
            return 0
        current += node.data
        target_sum = current - target
        total_paths = hash_table[target_sum] if target_sum in hash_table.keys() else 0
        self.increment_hash_table(hash_table, current, 1)
        total_paths += self.count_paths_with_sum_and_hash(node.left, target, current, hash_table)
        total_paths += self.count_paths_with_sum_and_hash(node.right, target, current, hash_table)
        self.increment_hash_table(hash_table, current, -1)
        return total_paths

    def increment_hash_table(self, hash_table, key, value):
        new_count = (hash_table[key] if key in hash_table.keys() else 0) + value
        if new_count == 0:
            hash_table.pop(key)
        else:
            hash_table[key] = new_count

tree = Tree(10)
print(tree.count_paths_with_sum(tree.root, 3))
print(tree.count_paths_with_sum2(5))
print(tree.count_paths_with_sum3(3))