class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])
    dsu = DSU(n)
    mst = []

    for u, v, w in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, w))

    return mst


edges = [
    (0, 1, 4), (0, 2, 3),
    (1, 2, 1), (1, 3, 2),
    (2, 3, 4)
]

print(kruskal(edges, 4))
