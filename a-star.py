import heapq

def a_star(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start, [start]))
    visited = set()

    while open_list: 
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            print("Path: ", " -> ".join(path))

            print("Total Cost: ", g)
            return 
        
        if current in visited: 
            continue

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    print("Goal not found")