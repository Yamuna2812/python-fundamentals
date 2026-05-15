def has_cycle(graph, node, visited, parent):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, node):
                return True
        elif parent != neighbor:
            return True

    return False


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

visited = set()

for node in graph:
    if node not in visited:
        if has_cycle(graph, node, visited, -1):
            print("Cycle detected")
            break
else:
    print("No cycle")
