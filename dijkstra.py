import heapq

def dijkstra(graph, start):
    # Initialize the distance for all nodes to infinity and distance to the start node as 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to hold the nodes to explore, initialized with the start node
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If the current distance is greater than the recorded distance, skip processing
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Only consider this path if it's better than the recorded distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example usage
if __name__ == "__main__":
    # Graph representation as an adjacency list where each node points to a dictionary
    # of neighbors and their respective edge weights
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    start_node = 'A'
    distances = dijkstra(graph, start_node)
    
    print("Shortest distances from node", start_node)
    for node, distance in distances.items():
        print(f"Node {node}: {distance}")
