class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


def clone_graph(node):
    visited = {}

    def dfs(n):
        if n in visited:
            return visited[n]

        copy = Node(n.val)
        visited[n] = copy

        for nei in n.neighbors:
            copy.neighbors.append(dfs(nei))

        return copy

    return dfs(node) if node else None
