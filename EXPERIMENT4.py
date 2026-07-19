import heapq
import time

def dijkstra(graph, source):

    distance = {vertex: float('inf') for vertex in graph}
    parent = {vertex: None for vertex in graph}

    distance[source] = 0

    priority_queue = [(0, source)]

    while priority_queue:

        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distance[current_vertex]:
            continue

        for neighbour, weight in graph[current_vertex]:

            new_distance = current_distance + weight

            if new_distance < distance[neighbour]:

                distance[neighbour] = new_distance
                parent[neighbour] = current_vertex

                heapq.heappush(priority_queue, (new_distance, neighbour))

    return distance, parent
def print_path(parent, vertex):

    path = []

    while vertex is not None:
        path.append(vertex)
        vertex = parent[vertex]

    return path[::-1]


print("=" * 65)
print("DIJKSTRA'S SHORTEST PATH ALGORITHM")
print("=" * 65)

vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

graph = {}

for i in range(vertices):
    graph[i] = []

print("\nEnter edges in the format: Source Destination Weight\n")

for i in range(edges):

    u, v, w = map(int, input(f"Edge {i+1}: ").split())

    graph[u].append((v, w))
    graph[v].append((u, w))     

source = int(input("\nEnter Source Vertex: "))
start = time.perf_counter()

distance, parent = dijkstra(graph, source)

elapsed = (time.perf_counter() - start) * 1000
print("\n")
print("=" * 75)
print("{:<10}{:<15}{:<35}".format(
    "Vertex",
    "Distance",
    "Shortest Path"))
print("=" * 75)

for vertex in range(vertices):

    if distance[vertex] == float('inf'):

        print("{:<10}{:<15}{:<35}".format(
            vertex,
            "INF",
            "No Path"))

    else:

        path = print_path(parent, vertex)

        print("{:<10}{:<15}{:<35}".format(
            vertex,
            distance[vertex],
            " -> ".join(map(str, path))))

print("=" * 75)

print("Execution Time : {:.6f} ms".format(elapsed))