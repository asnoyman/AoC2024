from math import inf

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.isCorrupted = False
        self.edges = []
        self.minDist = inf
    
    def __repr__(self):
        return f'{"#" if self.isCorrupted else '.', {len(self.edges)}}'

# Create a graph of size N x N where each node
N = 70
M = 1024
graph = []
for row in range(N + 1):
    graphRow = []
    for col in range(N + 1):
        graphRow.append(Node(row, col))
    graph.append(graphRow)
graph[0][0].minDist = 0

# Read in corrupted memory coords
# For the first M coords, record that those nodes are corrupted
with open('input.txt') as f:
    for i, line in enumerate(f.readlines()):
        if i == M:
            break

        col, row = [int(coord) for coord in line.strip().split(',')]
        graph[row][col].isCorrupted = True

# Create an edge between all uncorrupted nodes
for row, line in enumerate(graph):
    for col, node in enumerate(line):
        for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (row + delta[0] < 0 
                        or row + delta[0] > N 
                        or col + delta[1] < 0 
                        or col + delta[1] > N 
                        or graph[row + delta[0]][col + delta[1]].isCorrupted
                        or graph[row][col].isCorrupted):
                    continue
                node.edges.append(graph[row + delta[0]][col + delta[1]])


# print(*graph, sep='\n')

# BFS to find the shortest path length to the exit.
queue = [graph[0][0]]
while len(queue):
    node = queue.pop(0)
    for adjNode in node.edges:
        if node.minDist + 1 < adjNode.minDist:
            adjNode.minDist = node.minDist + 1
            queue.append(adjNode)

print(graph[N][N].minDist)

