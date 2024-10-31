import uuid
import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Зберігання кольору вузла
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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуємо значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_color="white")
    plt.show()


# Генерування унікальних кольорів
def generate_color(step, max_steps):
    start_color = (0, 0, 128)  # Темний синій
    end_color = (173, 216, 230)  # Світлий блакитний

    r = int(start_color[0] + (end_color[0] - start_color[0]) * (step / max_steps))
    g = int(start_color[1] + (end_color[1] - start_color[1]) * (step / max_steps))
    b = int(start_color[2] + (end_color[2] - start_color[2]) * (step / max_steps))

    return f'#{r:02x}{g:02x}{b:02x}'


# Обхід DFS
def dfs_collect_colors(root):
    stack = deque([root])
    visited = set()
    
    max_steps = count_nodes(root)
    step = 0

    # Присвоюємо кольори вузлам у порядку обходу
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            node.color = generate_color(step, max_steps)
            step += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


# Обхід BFS
def bfs_collect_colors(root):
    queue = Queue()
    queue.put(root)
    visited = set()
    
    max_steps = count_nodes(root)
    step = 0

    # Присвоюємо кольори вузлам у порядку обходу
    while not queue.empty():
        node = queue.get()
        if node not in visited:
            visited.add(node)
            node.color = generate_color(step, max_steps)
            step += 1
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)


# Підрахунок кількості вузлів у дереві
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Виконання обходу DFS і BFS з візуалізацією результатів
print("DFS traversal visualization:")
dfs_collect_colors(root)  # Присвоюємо відтінки для вузлів за обхід DFS
draw_tree(root)  # Візуалізуємо дерево для DFS

# Скидаємо кольори вузлів перед обходом BFS
root.color = "skyblue"
root.left.color = "skyblue"
root.left.left.color = "skyblue"
root.left.right.color = "skyblue"
root.right.color = "skyblue"
root.right.left.color = "skyblue"

print("\nBFS traversal visualization:")
bfs_collect_colors(root)  # Присвоюємо відтінки для вузлів за обхід BFS
draw_tree(root)  # Візуалізуємо дерево для BFS