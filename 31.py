class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


dsu = DSU(5)
dsu.union(0, 1)
dsu.union(1, 2)

print(dsu.find(2) == dsu.find(0))
