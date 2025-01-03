from collections import defaultdict
from itertools import combinations

# Create graph class
class Graph:

    edges = defaultdict(set)

    def addEdge(self, v1, v2):
        self.edges[v1].add(v2)
        self.edges[v2].add(v1)

    # Find all cycles of size 3
    def getAllTriangles(self, size=3):
        triangles = set()
        for v1 in self.edges:
            for v2 in self.edges[v1]:
                for v3 in self.edges[v2]:
                    if v3 in self.edges[v1]:
                        triangles.add(tuple(sorted([v1, v2, v3])))
        return triangles
    
    def getAllCliques(self, cliques, size):
        newCliques = set()
        for clique in cliques:
            for v in self.edges:
                valid = True
                for vertices in combinations(clique, size - 2):
                    if tuple(sorted([v] + [node for node in vertices])) not in cliques:
                        valid = False
                if valid:
                    newCliques.add(tuple(sorted([v] + [node for node in clique])))
        return newCliques


graph = Graph()
with open('input.txt') as f:
    for line in f.readlines():
        v1, v2 = line.strip().split('-')
        graph.addEdge(v1, v2)

cliques = graph.getAllTriangles()
size = 3
while True:
    newCliques = graph.getAllCliques(cliques, size + 1)

    if len(newCliques) == 0:
        break

    cliques = newCliques
    size += 1
    print(size, len(cliques))

print(','.join(cliques[0]))


# * This is much faster but I had no idea it existed until after finishing the question
# def bron_kerbosch(R, P, X, graph, cliques):
#     if not P and not X:  # Base case: R is a maximal clique
#         cliques.append(R)
#         return
    
#     for v in list(P):  # Iterating over a copy of P
#         bron_kerbosch(
#             R | {v}, 
#             P & set(graph.edges[v]), 
#             X & set(graph.edges[v]), 
#             graph, 
#             cliques
#         )
#         P.remove(v)
#         X.add(v)


# def find_maximal_cliques(graph):
#     R = set()
#     P = set(graph.edges.keys())
#     X = set()
#     cliques = []
#     bron_kerbosch(R, P, X, graph, cliques)
#     return max(cliques, key=len)

# print(','.join(sorted(list(find_maximal_cliques(graph)))))