"""
🔄 What is Topological Sort?
Topological Sort is a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge u → v, vertex u comes before vertex v in the ordering.

✅ When is it used?
Topological sort is used when you want to schedule tasks or resolve dependencies, like:
Course scheduling (you must take prerequisites first)
Build systems (some files must be compiled before others)
Task scheduling with dependencies

❗ Key Requirements:
The graph must be directed
The graph must be acyclic (i.e., no cycles)

🧠 Intuition:
If task A must be done before task B, then A should come before B in the sorted list.

📘 Example:
Given a DAG:

1 → 2 → 3
↓
4

One valid topological sort: 1, 4, 2, 3

🔧 Algorithms to Perform Topological Sort:
1. Kahn's Algorithm (BFS-based)

Count in-degrees (number of incoming edges) for each node
Start with nodes of in-degree 0
Remove them, reduce in-degrees of neighbors
Keep repeating

2. DFS-based

Do DFS
Add nodes to a stack after visiting all descendants
Reverse the stack at the end

🧪 DFS-based Python Example:
"""
def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # reverse the stack

graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    1: [],
    0: []
}
print(topological_sort_dfs(graph))
# Possible output: [4, 5, 2, 3, 1, 0]
