import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, []).append(to_node)
        self.distances[(from_node, to_node)] = distance

def dijkstra(graph, initial_node):
    visited = {initial_node: 0}
    heap = [(0, initial_node)]

    while heap:
        (current_distance, current_node) = heapq.heappop(heap)

        for neighbor in graph.edges.get(current_node, []):
            new_distance = visited[current_node] + graph.distances[(current_node, neighbor)]
            if neighbor not in visited or new_distance < visited[neighbor]:
                visited[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return visited

# Приклад використання:
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")

graph.add_edge("A", "B", 5)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "D", 4)
graph.add_edge("C", "B", 1)
graph.add_edge("C", "D", 6)
graph.add_edge("C", "E", 3)
graph.add_edge("D", "E", 7)

initial_node = "A"
shortest_paths = dijkstra(graph, initial_node)
print("Найкоротші відстані від вершини", initial_node, "до інших вершин:")
for node, distance in shortest_paths.items():
    print(f"Від {initial_node} до {node}: {distance}")
