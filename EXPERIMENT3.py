import heapq
import time

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y

        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x

        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

def kruskal(vertices, edges):

    edges.sort()

    uf = UnionFind(vertices)

    mst = []
    total_cost = 0

    for weight, u, v in edges:

        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

        if len(mst) == vertices - 1:
            break

    return mst, total_cost

def prim(vertices, graph):

    visited = [False] * vertices

    pq = [(0, 0, -1)]          

    mst = []

    total_cost = 0

    while pq:

        weight, current, parent = heapq.heappop(pq)

        if visited[current]:
            continue

        visited[current] = True

        if parent != -1:
            mst.append((parent, current, weight))
            total_cost += weight

        for neighbour, wt in graph[current]:
            if not visited[neighbour]:
                heapq.heappush(pq, (wt, neighbour, current))

    return mst, total_cost
print("=" * 60)
print("MINIMUM SPANNING TREE")
print("=" * 60)

vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

edges = []
graph = {}

for i in range(vertices):
    graph[i] = []

print("\nEnter edges in the format: Source Destination Weight\n")

for i in range(edges_count):

    u, v, w = map(int, input(f"Edge {i+1}: ").split())

    edges.append((w, u, v))

    graph[u].append((v, w))
    graph[v].append((u, w))


start = time.perf_counter()

k_mst, k_cost = kruskal(vertices, edges)

k_time = (time.perf_counter() - start) * 1000


start = time.perf_counter()

p_mst, p_cost = prim(vertices, graph)

p_time = (time.perf_counter() - start) * 1000
print("\n")
print("=" * 60)
print("KRUSKAL'S MST")
print("=" * 60)

for u, v, w in k_mst:
    print(f"{u} ---- {v}   Weight = {w}")

print("Total Cost =", k_cost)
print("Execution Time = {:.6f} ms".format(k_time))


print("\n")
print("=" * 60)
print("PRIM'S MST")
print("=" * 60)

for u, v, w in p_mst:
    print(f"{u} ---- {v}   Weight = {w}")

print("Total Cost =", p_cost)
print("Execution Time = {:.6f} ms".format(p_time))


print("\n")
print("=" * 60)

if k_cost == p_cost:
    print("Verification Successful")
    print("Both algorithms produced the SAME Minimum Spanning Tree Cost.")

else:
    print("Verification Failed")
    print("The MST costs are different.")

print("=" * 60)