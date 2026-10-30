from collections import deque

def shortest_path(graph, start, target):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == target:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append(new_path)

    return None


# Example
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

print(shortest_path(graph, "A", "F"))