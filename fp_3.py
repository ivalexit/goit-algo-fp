""" 
 Імітація платформи, що визначає рівень генетичної спорідненості користувачів
на основі результатів генетичного тесту. Для визначення найближчих родичів (найкоротших шляхів)
 серед користувачів платформи використано алгоритм Дейкстри.
  Кількість вузлів (зразків для тестування) може бути введено, в іншому випадку число
  буде згенеровано автоматично в межах 5-20.

"""


import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq
from itertools import combinations

# Функція для запиту кількості генетичних тестів.
# Лабораторія приймає на обробку не менше 5 і не більше 20 зразків ДНК за раз.
def get_user_count():
    try:
        user_input = input("Enter the number of DNA samples (or press Enter for a random count between 5 and 20): ")
        if user_input.strip() == "":
            return random.randint(5, 20)
        user_count = int(user_input)
        if 5 <= user_count <= 20:
            return user_count
        else:
            print("Please enter a number between 5 and 20.")
            return get_user_count()
    except ValueError:
        print("Invalid input. Please enter a number between 5 and 20.")
        return get_user_count()

# Функція для імітації генетичного тесту
def simulate_genetic_test(users):
    connections = []
    for user1, user2 in combinations(users, 2):
        closeness_level = random.randint(1, 100)  # Чим менше значення, тим ближчі родичі
        connections.append((user1, user2, closeness_level))
    return connections

# Створюємо граф і додаємо вершини (користувачів) та зважені ребра (родинні зв’язки)
def create_genetic_graph(users, connections):
    GeneticConnections = nx.DiGraph()
    GeneticConnections.add_nodes_from(users)

    for u, v, weight in connections:
        GeneticConnections.add_edge(u, v, weight=weight)
        GeneticConnections.add_edge(v, u, weight=weight)  # Користувачі споріднені взаємно
    
    return GeneticConnections

# Візуалізація графа з вагами
def visualize_genetic_graph(graph):
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color="green", 
            node_size=1100, font_size=10, font_weight="bold", edge_color="purple", arrows=True)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title("Genetic Connection Platform with random relationship strengths")
    plt.show()

# Реалізація алгоритму Дейкстри для знаходження найближчих родичів
def dijkstra_with_heap(graph, start_node):
    min_heap = [(0, start_node)]
    distances = {node: float('inf') for node in graph.nodes}
    distances[start_node] = 0
    
    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    
    return distances

# Генеруємо кількість користувачів на основі введення або випадково згенерованого числа
num_users = get_user_count()
users = [f'User{i}' for i in range(1, num_users + 1)]

# Генеруємо зв’язки на основі результатів "генетичного тесту"
connections = simulate_genetic_test(users)

# Створюємо граф на основі результатів "генетичного тесту"
GeneticConnections = create_genetic_graph(users, connections)

# Візуалізуємо граф спорідненості
visualize_genetic_graph(GeneticConnections)

# Використання алгоритму Дейкстри для кожного користувача
closest_relations = {}
for user in GeneticConnections.nodes:
    closest_relations[user] = dijkstra_with_heap(GeneticConnections, user)

# Виведення результатів
print("Closest genetic relations for each user based on simulated genetic test:")
for start_user, relations in closest_relations.items():
    print(f"From {start_user}:")
    for target, closeness in relations.items():
        print(f"  To {target} - Closeness level (lower is closer): {closeness}")
    print()