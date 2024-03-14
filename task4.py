import uuid
import networkx as nx
import matplotlib.pyplot as plt

class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_heap_edges(graph, heap, pos, i, x=0, y=0, layer=1):
    if i < len(heap):
        graph.add_node(heap[i].id, color=heap[i].color, label=heap[i].val)  # Використання id та збереження значення вузла
        if 2 * i + 1 < len(heap):
            graph.add_edge(heap[i].id, heap[2 * i + 1].id)
            l = x - 1 / 2 ** layer
            pos[heap[2 * i + 1].id] = (l, y - 1)
            add_heap_edges(graph, heap, pos, 2 * i + 1, x=l, y=y - 1, layer=layer + 1)
        if 2 * i + 2 < len(heap):
            graph.add_edge(heap[i].id, heap[2 * i + 2].id)
            r = x + 1 / 2 ** layer
            pos[heap[2 * i + 2].id] = (r, y - 1)
            add_heap_edges(graph, heap, pos, 2 * i + 2, x=r, y=y - 1, layer=layer + 1)

def draw_heap(heap):
    heap_graph = nx.DiGraph()
    pos = {heap[0].id: (0, 0)}
    add_heap_edges(heap_graph, heap, pos, 0)

    colors = [node[1]['color'] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap_graph.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(heap_graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Приклад використання:
heap = [HeapNode(0), HeapNode(4), HeapNode(1), HeapNode(5), HeapNode(3), HeapNode(10)]

# Відображення бінарної купи
draw_heap(heap)
