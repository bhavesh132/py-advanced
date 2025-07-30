from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue: 
        node = queue.popleft()
        if node not in visited: 
            print(node, end= " ")
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(neighbor)


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack: 
        node = stack.pop()
        if node not in visited: 
            print(node, end= " ")
            visited.add(node)
            for neighbor in reversed(graph[node]):
                stack.append(neighbor)