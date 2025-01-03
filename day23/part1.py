from collections import defaultdict

# Create graph class
class Graph:

    edges = defaultdict(set)

    def addEdge(self, v1, v2):
        self.edges[v1].add(v2)
        self.edges[v2].add(v1)

    # Find all cycles of size 3
    def getAllCycles(self, size=3):
        cycles = set()
        for v1 in self.edges:
            for v2 in self.edges[v1]:
                for v3 in self.edges[v2]:
                    if v3 in self.edges[v1]:
                        cycles.add(tuple(sorted([v1, v2, v3])))
        return cycles
    
graph = Graph()
with open('input.txt') as f:
    for line in f.readlines():
        v1, v2 = line.strip().split('-')
        graph.addEdge(v1, v2)

cycles = graph.getAllCycles()

tally = sum(any(computer[0] == 't' for computer in cycle) for cycle in cycles)
print(tally)