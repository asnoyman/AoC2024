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


# Read in corrupted memory coords
corruptedMemory = []
with open('input.txt') as f:
    for line in f.readlines():
        corruptedMemory.append([int(coord) for coord in line.strip().split(',')])

# Create an edge between all nodes
for row, line in enumerate(graph):
    for col, node in enumerate(line):
        for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (row + delta[0] < 0 
                        or row + delta[0] > N 
                        or col + delta[1] < 0 
                        or col + delta[1] > N):
                    continue
                node.edges.append(graph[row + delta[0]][col + delta[1]])

# Until the path is blocked, corrupt the next cell, remove its edges, reset the grid and check for a path
while True:
    corruptedCol, corruptedRow = corruptedMemory.pop(0)
    graph[corruptedRow][corruptedCol].isCorrupted = True
    for adjNode in graph[corruptedRow][corruptedCol].edges:
        adjNode.edges.remove(graph[corruptedRow][corruptedCol])
    graph[corruptedRow][corruptedCol].edges = []

    for row in graph:
        for node in row:
            node.minDist = inf
    graph[0][0].minDist = 0

    # BFS to find the shortest path length to the exit.
    queue = [graph[0][0]]
    while len(queue):
        node = queue.pop(0)
        for adjNode in node.edges:
            if node.minDist + 1 < adjNode.minDist:
                adjNode.minDist = node.minDist + 1
                queue.append(adjNode)
    
    # If no path was found to the exit, print the coordinates and stop running
    if graph[N][N].minDist == inf:
        print(f"{corruptedCol},{corruptedRow}")
        break

