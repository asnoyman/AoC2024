from math import inf
from queue import PriorityQueue

WALL = '#'
EMPTY = '.'

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Node:
    def __init__(self, row, col, value, minTime):
        self.row = row
        self.col = col
        self.value = value
        self.edges = dict()
        self.minTime = minTime

    def __repr__(self):
        return f'(row: {self.row}, col: {self.col}, {self.value})'
    
    def __lt__(self, node):
        return True


def getRotationCost(dir1, dir2):
    if dir1 == dir2:
        return 0
    elif abs(dir1 - dir2) == 2:
        return 2000
    else:
        return 1000

# Read input into graph
# Note start and end coords
# Create nodes at each character in the input 
graph = []
startPoint = None
endPoint = None
with open('input.txt') as f:
    for i, row in enumerate(f.readlines()):
        graphRow = []
        for j, col in enumerate(row.strip()):
            if col in ('#', '.'):
                graphRow.append(Node(i, j, col, [inf, inf, inf, inf]))
            if col == 'S':
                graphRow.append(Node(i, j, EMPTY, [1000, 0, 1000, 2000]))
                startPoint = (i, j)
            if col == 'E':
                graphRow.append(Node(i, j, EMPTY, [inf, inf, inf, inf]))
                endPoint = (i, j)
        graph.append(graphRow)

# print(*graph, sep='\n')
# print(startPoint, endPoint)

# Create undirected edges from each non-wall to each other orthogonal non-wall
for i, row in enumerate(graph):
    for j, node in enumerate(row):
        if node.value == WALL:
            continue
        if i != 0 and graph[i - 1][j].value == EMPTY:
            node.edges[UP] = graph[i - 1][j]
        if i != len(graph) - 1 and graph[i + 1][j].value == EMPTY:
            node.edges[DOWN] = graph[i + 1][j]
        if j != 0 and graph[i][j - 1].value == EMPTY:
            node.edges[LEFT] = graph[i][j - 1]
        if j != len(graph) - 1 and graph[i][j + 1].value == EMPTY:
            node.edges[RIGHT] = graph[i][j + 1]

# print(*graph, sep='\n')


# Find shortest time to each empty cell from start
pq = PriorityQueue()
pq.put((0, graph[startPoint[0]][startPoint[1]], RIGHT))

while not pq.empty():
    time, node, direction = pq.get()
    # print(time, node)

    if time > node.minTime[direction]:
        continue

    for dir, neighbour in node.edges.items():
        costToMove = node.minTime[direction] + getRotationCost(direction, dir) + 1
        
        if costToMove < neighbour.minTime[dir]:
            neighbour.minTime[dir] = costToMove
            pq.put((costToMove, neighbour, dir))


# Print shortest time to end point
print(min(graph[endPoint[0]][endPoint[1]].minTime))