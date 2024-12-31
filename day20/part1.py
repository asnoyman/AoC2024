from itertools import permutations
from collections import defaultdict

class Node:
    def __init__(self, value):
        """
        Initialize a Node.
        :param value: The value of the node.
        """
        self.value = value
        self.neighbors = {}  # Dictionary to store neighbors and their weights

    def add_neighbor(self, neighbor, weight):
        """
        Add a neighbor to the node with the given weight.
        :param neighbor: The neighbor node.
        :param weight: The weight of the edge.
        """
        self.neighbors[neighbor] = weight

    def __str__(self):
        """
        String representation of the node and its neighbors.
        """
        return f"Node({self.value}): {[(n.value, w) for n, w in self.neighbors.items()]}"


class Graph:
    def __init__(self):
        """
        Initialize a Graph.
        """
        self.nodes = {}

    def add_node(self, value):
        """
        Add a node to the graph.
        :param value: The value of the node.
        :return: The created node.
        """
        if value not in self.nodes:
            self.nodes[value] = Node(value)
        return self.nodes[value]

    def add_edge(self, from_value, to_value, weight=1):
        """
        Add a directed edge to the graph.
        :param from_value: The starting node value.
        :param to_value: The ending node value.
        :param weight: The weight of the edge.
        """
        from_node = self.add_node(from_value)
        to_node = self.add_node(to_value)
        from_node.add_neighbor(to_node, weight)

    def __str__(self):
        """
        String representation of the graph.
        """
        return "\n".join(str(node) for node in self.nodes.values())


# Dijkstra's Algorithm Using Graph and Node Classes
import heapq

def dijkstra(graph, start_value):
    """
    Finds the shortest path from a start node to all other nodes in the graph.
    :param graph: The Graph object.
    :param start_value: The starting node value.
    :return: A dictionary of shortest distances to each node.
    """
    start_node = graph.nodes.get(start_value)
    if not start_node:
        raise ValueError(f"Start node {start_value} not found in the graph.")

    # Initialize distances with infinity for all nodes, except the start node
    distances = {node: float('inf') for node in graph.nodes.values()}
    distances[start_node] = 0

    # Priority queue to store (distance, node)
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip nodes that have already been processed with a shorter distance
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in current_node.neighbors.items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Convert distances to a readable format
    return {node.value: dist for node, dist in distances.items()}

def getAdjacentEmptyCells(grid, row, col):
    adjCells = []
    for delta in [(1, 0), (0, 1), (-1,0), (0,-1)]:
        if (row + delta[0] < 0 
                or row + delta[0] >= len(grid) 
                or col + delta[1] < 0 
                or col + delta[1] >= len(grid[0]) 
                or grid[row + delta[0]][col + delta[1]] == '#'):
            continue
        adjCells.append((row + delta[0], col + delta[1]))
    return adjCells


# Create graph from input
# Record edges in graph
# Create list of all possible cheats ((wallRow, wallCol), (emptyRow, emptyCol))
grid = []
with open('input.txt') as f:
    for row, line in enumerate(f.readlines()):
        grid.append(line.strip())

graph = Graph()
shortCuts = []
startPos = None
endPos = None
for row, line in enumerate(grid):
    for col, cell in enumerate(line):
        adjList = getAdjacentEmptyCells(grid, row, col)
        if cell == '#':
            shortCuts.extend(permutations(adjList, 2))
        else:
            for adjCell in adjList:
                graph.add_edge((row, col), adjCell)
            if cell == 'S':
                startPos = (row, col)
            if cell == 'E':
                endPos = (row, col)

shortestDistancesFromStart = dijkstra(graph, startPos)
shortestDistancesFromEnd = dijkstra(graph, endPos)

minLegalDist = shortestDistancesFromStart[endPos]
shortCutDict = defaultdict(int)
numSavedOver100 = 0
for start, end in shortCuts:
    shortCutSavings = minLegalDist - (shortestDistancesFromStart[start] + shortestDistancesFromEnd[end] + 2)

    if shortCutSavings > 0:
        shortCutDict[shortCutSavings] += 1
    if shortCutSavings >= 100:
        numSavedOver100 += 1

print(numSavedOver100)