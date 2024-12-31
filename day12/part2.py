from collections import defaultdict
from queue import PriorityQueue

class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.edges = defaultdict(Node)
        self.visited = False

    def __repr__(self):
        return f'{self.value}, {[e.value for e in self.edges.values()]}'
    

def mergeOverlappingSides(sides):
    sideCount = 0
    for pq in sides.values():
        while not pq.empty():
            sideA = pq.get()
            if pq.empty():
                sideCount += 1
                break

            sideB = pq.get()

            if sideA[1] == sideB[0]:
                pq.put((sideA[0], sideB[1]))
            else:
                sideCount += 1
                pq.put(sideB)
    return sideCount


# Read grid into graph with edges connecting groups
graph = []
with open('input.txt') as f:
    for i, row in enumerate(f.readlines()):
        graphRow = []
        for j, node in enumerate(row.strip()):
            graphRow.append(Node(i, j, node))
        graph.append(graphRow)


# Create edges between nodes that can be travelled between
for i, row in enumerate(graph):
    for j, node in enumerate(row):
        if i - 1 >= 0 and graph[i-1][j].value == node.value:
            node.edges['UP'] = graph[i-1][j]
        if i + 1 < len(graph) and graph[i+1][j].value == node.value:
            node.edges['DOWN'] = graph[i+1][j]
        if j - 1 >= 0 and graph[i][j-1].value == node.value:
            node.edges['LEFT'] = graph[i][j-1]
        if j + 1 < len(graph[0]) and graph[i][j+1].value == node.value:
            node.edges['RIGHT'] = graph[i][j+1]


# For each group, calculate side count and area
total = 0
for row in graph:
    for node in row:
        area = 0
        sides = defaultdict(PriorityQueue)
        queue = [node]
        while len(queue):
            n = queue.pop(0)
            if n.visited:
                continue
            n.visited = True
            area += 1

            # For each direction, if there is an edge, lengthen the existing side
            # or create a new side if one does note exist
            if 'UP' not in n.edges.keys():
                sides[(n.row, 'UP')].put((n.col, n.col + 1))
            if 'RIGHT' not in n.edges.keys():
                sides[(n.col + 1, 'RIGHT')].put((n.row, n.row + 1))
            if 'DOWN' not in n.edges.keys():
                sides[(n.row + 1, 'DOWN')].put((n.col, n.col + 1))
            if 'LEFT' not in n.edges.keys():
                sides[(n.col, 'LEFT')].put((n.row, n.row + 1))

            queue += n.edges.values()

        sideCount = mergeOverlappingSides(sides)

        total += area * sideCount

# Print the sum of the products of each S and A
print(total)