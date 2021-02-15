class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self, size):
        self.root_map = {}
        self.root = self.make_BST(0, size - 1, None)

    def make_BST(self, start, end, parent):
        if start > end:
            return None
        mid = (start + end) // 2
        node = self.Node(mid)
        node.left = self.make_BST(start, mid - 1, node)
        node.right = self.make_BST(mid + 1, end, node)
        node.parent = parent
        self.root_map[mid] = node
        return node

    def get_node(self, data):
        return self.root_map[data]

    def common_ancestor(self, d1, d2):
        p = self.get_node(d1)
        q = self.get_node(d2)
        diff = self.depth(p) - self.depth(q)

        first = q if diff > 0 else p
        second = p if diff > 0 else q
        second = self.go_up_by(second, abs(diff))

        while first != second and first != None and second != None:
            first = first.parent
            second = second.parent

        return None if first == None or second == None else first

    def go_up_by(self, node, diff):
        while diff > 0 and node != None:
            node = node.parent
            diff -= 1
        return node

    def depth(self, node):
        d = 0
        while node != None:
            node = node.parent
            d += 1
        return d

    def covers(self, root, node):
        if root == None:
            return False
        if root == node:
            return True

        return self.covers(root.left, node) or self.covers(root.right, node)

    def common_ancestor2(self, d1, d2):
        p = self.get_node(d1)
        q = self.get_node(d2)
        if not self.covers(self.root, p) or not self.covers(self.root, q):
            return None
        elif self.covers(p, q):
            return p
        elif self.covers(q, p):
            return q
        sibling = self.get_sibling(p)
        parent = p.parent
        while not self.covers(sibling, q):
            sibling = self.get_sibling(parent)
            parent = parent.parent
        return parent

    def get_sibling(self, node):
        if node == None or node.parent == None:
            return None
        parent = node.parent
        return parent.right if parent.left == node else parent.left

    def common_ancestor3(self, d1, d2):
        p = self.get_node(d1)
        q = self.get_node(d2)
        if not self.covers(self.root, p) or not self.covers(self.root, q):
            return None
        return self.ancestor_helper(self.root, p, q)

    def ancestor_helper(self, root, p, q):
        if root == None or root == p or root == q:
            return self.root
        p_is_on_left = self.covers(root.left, p)
        q_is_on_left = self.covers(root.left, q)
        if p_is_on_left != q_is_on_left:
            return root
        chlid_side = root.left if p_is_on_left else root.right
        return self.ancestor_helper(chlid_side, p, q)

    def common_ancestor4(self, d1, d2):
        p = self.get_node(d1)
        q = self.get_node(d2)
        return self.common_ancestor_without_parent(self.root, p, q)

    def common_ancestor_without_parent(self, root, p, q):
        if root == None:
            return None
        if root == p and root == q:
            return root
        x = self.common_ancestor_without_parent(root.left, p, q)
        if x != None and x != p and x != q:
            return x
        y = self.common_ancestor_without_parent(root.right, p, q)
        if y != None and y != p and y != q:
            return y

        if x != None and y != None:
            return root
        elif root == p or root == q:
            return root
        else:
            return y if x == None else x

    class Result:
        def __init__(self, n, is_anc):
            self.node = n
            self.is_ancestor = is_anc

    def common_ancestor5(self, d1, d2):
        p = self.get_node(d1)
        q = self.get_node(d2)
        r = self.common_ancestor_without_parent2(self.root, p, q)
        if r.is_ancestor:
            return r.node
        return None

    def common_ancestor_without_parent2(self, root, p, q):
        if root == None:
            return self.Result(None, False)
        if root == p and root == q:
            return self.Result(root, True)
        rx = self.common_ancestor_without_parent2(root.left, p, q)
        if rx.is_ancestor:
            return rx
        ry = self.common_ancestor_without_parent2(root.right, p, q)
        if ry.is_ancestor:
            return ry

        if rx.node != None and ry.node != None:
            return self.Result(root, True)
        elif root == p or root == q:
            is_ancestor = rx.node != None or ry.node != None
            return self.Result(root, is_ancestor)
        else:
            return self.Result(rx.node if rx.node != None else ry.node, False)

t = Tree(10)
fa = t.common_ancestor(3, 5)
print("The first common ancestor is", fa.data)
fa2 = t.common_ancestor2(0, 3)
print("The first common ancestor is", fa2.data)
fa3 = t.common_ancestor3(2, 8)
print("The first common ancestor is", fa3.data)
fa4 = t.common_ancestor4(6, 8)
print("The first common ancestor is", fa4.data)
fa5 = t.common_ancestor5(0, 3)
print("The first common ancestor is", fa5.data)

