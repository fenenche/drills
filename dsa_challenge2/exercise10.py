from collections import deque

def path_exists(graph, start, target):
    if start == target:
        return True
    queue = deque([start])
    visited = {start}
    
    while queue:
        current_node = queue.popleft()
        
        for neighbor in graph.get(current_node, []):
            if neighbor == target:
                return True
                
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return False

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}
my_lists = path_exists(graph, start = "A", target = "F")
my_list2 = path_exists(graph, start = "D", target = "A")
print(my_lists)
print(my_list2)
