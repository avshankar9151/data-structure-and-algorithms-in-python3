'''
DFS & BFS (Graph Traversal)
------------------------------------------
Use when:

- Graph problems (connected components, shortest path in unweighted graph)

- Tree traversals

- Grid/Matrix problems (islands, flood fill, shortest path in maze)
------------------------------------------
⚡ Rule of thumb:

- Use DFS → explore paths fully (recursion/backtracking).

- Use BFS → shortest path in unweighted graphs or levels.
------------------------------------------
'''
from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nei in graph[start]:
        if nei not in visited:
            dfs(graph, nei, visited)
    return visited

def bfs(graph, start):
    visited = set([start])
    q = deque([start])
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
    return visited
