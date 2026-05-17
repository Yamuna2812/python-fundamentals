from collections import deque

def can_finish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    indegree = [0]*numCourses

    for u, v in prerequisites:
        graph[v].append(u)
        indegree[u] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])

    count = 0
    while queue:
        node = queue.popleft()
        count += 1

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return count == numCourses


print(can_finish(2, [[1, 0]]))
