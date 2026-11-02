# PR2: Depth First Search (DFS)

```python
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

# DFS Algorithm
def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    nodes_explored = 0

    while stack:
        path = stack.pop()
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)
        nodes_explored += 1

        if node == goal:
            return path, nodes_explored

        # Reverse order for predictable DFS traversal
        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                new_path = path + [neighbour]
                stack.append(new_path)

    return None, nodes_explored

# Execute DFS
start_time = time.perf_counter()

dfs_path, dfs_nodes = dfs(graph, start, goal)

dfs_time = time.perf_counter() - start_time

# Display Results
print("========== DFS RESULTS ==========")
print("Path:", " -> ".join(dfs_path))
print("Path Length:", len(dfs_path) - 1)
print("Nodes Explored:", dfs_nodes)
print("Execution Time: {:.8f} seconds".format(dfs_time))
```

**Expected Output:**

```text
========== DFS RESULTS ==========
Path: A -> B -> D -> G
Path Length: 3
Nodes Explored: 4
Execution Time: (varies) seconds
```

**Result:** Depth First Search successfully finds a path from the starting node A to the goal node G.
