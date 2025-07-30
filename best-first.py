import heapq

def best_first(graph, heuristics, start, goal):
    visited = set()
    queue = []
    heapq.heappush(queue, (heuristics[start], start))

    while queue:
        cost, node = heapq.heappop(queue)
        if node in visited: 
            continue

        print(f"visited node {node}")
        visited.add(node)

        if node == goal:
            print(f"Found goal {goal} with cost {cost}")
            return
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (heuristics[neighbor], neighbor))
    
    print ("Goal not found")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristics = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 2,
    'F': 0
}

best_first(graph, heuristics, 'A', 'F')