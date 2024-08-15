import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Створення власного вагового графа
G = nx.Graph()
G.add_edge("A", "B", weight=4)
G.add_edge("A", "C", weight=2)
G.add_edge("B", "C", weight=5)
G.add_edge("B", "D", weight=10)
G.add_edge("C", "E", weight=3)
G.add_edge("E", "D", weight=4)
G.add_edge("D", "F", weight=11)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізуємо відстані до всіх вершин як нескінченність
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    # Відстань до початкової вершини дорівнює 0
    shortest_paths[start] = 0
    # Ініціалізуємо бінарну купу з початковою вершиною
    priority_queue = [(0, start)]

    while priority_queue:
        # Витягуємо вузол з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо знайдений шлях до поточного вузла не є оптимальним, пропускаємо його
        if current_distance > shortest_paths[current_vertex]:
            continue

        # Оновлюємо відстань до сусідів поточного вузла
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes["weight"]
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда, оновлюємо його
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

# Використання алгоритму Дейкстри
shortest_paths = dijkstra(G, "A")
print("Найкоротші шляхи від вершини A:", shortest_paths)

# Візуалізація графа
pos = nx.spring_layout(G)  # Визначення позицій для всіх вузлів
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()
