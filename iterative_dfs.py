def dls(graph, node, target, depth, visited): # Depth Limited Search
    if depth == 0:
        return node == target
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            if dls(graph, neighbor, target, depth -1, visited):
                return True
    return False

def iddfs(graph, start, target, max_depth):
    for depth in range(max_depth+1):
        visited = set()
        print(f"Searching at Depth {depth}")
        if dls(graph, start, target, depth, visited):
            print(f"Found target {target} at depth {depth}")
            return True
        print("Target Not Found")
    return False