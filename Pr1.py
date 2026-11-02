# PR1: Breadth First Search (BFS)

```python
from collections import deque
import time

# Graph representing routes between locations
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

start = 'A'
goal = 'G'

# BFS Algorithm
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    nodes_explored = 0

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)
        nodes_explored += 1

        if node == goal:
            return path, nodes_explored

        for neighbour in graph[node]:
            if neighbour not in visited:
                new_path = path + [neighbour]
                queue.append(new_path)

    return None, nodes_explored

# Execute BFS
start_time = time.perf_counter()

bfs_path, bfs_nodes = bfs(graph, start, goal)

bfs_time = time.perf_counter() - start_time

# Display Results
print("========== BFS RESULTS ==========")
print("Path:", " -> ".join(bfs_path))
print("Path Length:", len(bfs_path) - 1)
print("Nodes Explored:", bfs_nodes)
print("Execution Time: {:.8f} seconds".format(bfs_time))
```

**Expected Output:**

```text
========== BFS RESULTS ==========
Path: A -> B -> D -> G
Path Length: 3
Nodes Explored: 7
Execution Time: (varies) seconds
```

**Result:** Breadth First Search successfully finds the shortest path from the starting node A to the goal node G.
