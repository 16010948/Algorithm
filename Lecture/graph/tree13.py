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

def all_sequences(node):
    result = []
    if node == None:
        result.append([])
        return result
    prefix = []
    prefix.append(node.data)

    left_seq = all_sequences(node.left)
    right_seq = all_sequences(node.right)

    for left in left_seq:
        for right in right_seq:
            weaved = []
            weave_lists(left, right, weaved, prefix)
            result += weaved
    return result

def weave_lists(first, second, results, prefix):
    if len(first) == 0 or len(second) == 0:
        result = []
        for data in prefix:
            result.append(data)
        result += first
        result += second
        results.append(result)
        return
    head_first = first.pop(0)
    prefix.append(head_first)
    weave_lists(first, second, results, prefix)
    prefix.pop()
    first.insert(0, head_first)

    head_second = second.pop(0)
    prefix.append(head_second)
    weave_lists(first, second, results, prefix)
    prefix.pop()
    second.insert(0, head_second)

t = Tree(6)
result = all_sequences(t.root)
for l in result:
    for data in l:
        print(data, end=" ")
    print()
