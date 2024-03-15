import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def depth_first_traversal(node, colors):
    if node is None:
        return
    colors[node.id] = calculate_color(len(colors))
    depth_first_traversal(node.left, colors)
    depth_first_traversal(node.right, colors)

def breadth_first_traversal(root, colors):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            colors[node.id] = calculate_color(len(colors))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def calculate_color(step):
    # Генеруємо RGB колір на основі кроку обходу
    r = int(255 * (step / 255))
    g = int(150 * (step / 255))
    b = int(240 * (step / 255))
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

def draw_tree_traversal(root, traversal_type):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)

    colors = {}
    if traversal_type == "depth":
        depth_first_traversal(root, colors)
    elif traversal_type == "breadth":
        breadth_first_traversal(root, colors)

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=list(colors.values()))
    plt.show()

# Приклад використання:
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення обходу у глибину
draw_tree_traversal(root, "depth")

# Відображення обходу в ширину
draw_tree_traversal(root, "breadth")
