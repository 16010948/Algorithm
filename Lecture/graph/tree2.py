class Graph:
    class Node:
        def __init__(self, data):
            self.data = data
            self.marked = False
            self.adjacent = []

    def __init__(self, size):
        self.nodes = [0] * size
        for i in range(size):
            self.nodes[i] = self.Node(i)

    def add_edge(self, i1, i2):
        n1 = self.nodes[i1]
        n2 = self.nodes[i2]

        if n2 not in n1.adjacent:
            n1.adjacent.append(n2)

        if n1 not in n2.adjacent:
            n2.adjacent.append(n1)

    def dfs(self, index):
        root = self.nodes[index]
        stack = []
        stack.append(root)
        root.marked = True
        while len(stack) > 0:
            r = stack.pop()
            for n in r.adjacent:
                if n.marked == False:
                    n.marked = True
                    stack.append(n)
            self.visit(r)

    def bfs(self, index):
        root = self.nodes[index]
        queue = []
        queue.append(root)
        root.marked = True
        while len(queue) > 0:
            r = queue.pop(0)
            for n in r.adjacent:
                if n.marked == False:
                    n.marked = True
                    queue.append(n)
            self.visit(r)

    def dfs_recursive(self, r):
        if r == None:
            return
        r.marked = True
        self.visit(r)
        for n in r.adjacent:
            if n.marked == False:
                self.dfs_recursive(n)


    def visit(self, n):
        print(n.data, end=" ")

g = Graph(9)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(5, 6)
g.add_edge(5, 7)
g.add_edge(6, 8)

# g.dfs(0)
# g.bfs(0)
g.dfs_recursive(g.nodes[3])