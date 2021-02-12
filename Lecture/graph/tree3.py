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

    def init_marks(self):
        for n in self.nodes:
            n.marked = False

    def search(self, i1, i2):
        start = self.nodes[i1]
        end = self.nodes[i2]
        self.init_marks()

        q = []
        q.append(start)
        while len(q) > 0:
            root = q.pop(0)
            if root == end:
                return True
            for n in root.adjacent:
                if n.marked == False:
                    n.marked = True
                    q.append(n)
        return False

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
print(g.search(1, 8))