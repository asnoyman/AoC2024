class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.edges = []
    
    def __repr__(self):
        return f'{self.value}, {[e.value for e in self.edges]}'


# Read input as a graph with nodes at each position on the map
# and a directed edge to nodes with value one higher than themselves
# Create a list of the trailheads (0s) and endpoints (9s)
graph = []
starts = []
ends = []
with open('input.txt') as f:
    for i, row in enumerate(f.readlines()):
        graphRow = []
        for j, node in enumerate(row.strip()):
            if node == '0':
                starts.append((i, j))
            if node == '9':
                ends.append((i, j))
            graphRow.append(Node(i, j, int(node)))
        graph.append(graphRow)


# Create edges between nodes that can be travelled between
for i, row in enumerate(graph):
    for j, node in enumerate(row):
        if i - 1 >= 0 and graph[i-1][j].value == node.value + 1:
            node.edges.append(graph[i-1][j])
        if i + 1 < len(graph) and graph[i+1][j].value == node.value + 1:
            node.edges.append(graph[i+1][j])
        if j - 1 >= 0 and graph[i][j-1].value == node.value + 1:
            node.edges.append(graph[i][j-1])
        if j + 1 < len(graph[0]) and graph[i][j+1].value == node.value + 1:
            node.edges.append(graph[i][j+1])


# Check the graph to see how many unique endpoints can be reached by each trail head
# Simple DFS to find all unique endpoints
total = 0
for start in starts:
    endsFound = set()
    stack = [node for node in graph[start[0]][start[1]].edges]
    while len(stack):
        currPos = stack.pop()
        if currPos.value == 9:
            endsFound.add(currPos)
        stack += [node for node in graph[currPos.row][currPos.col].edges]
    total += len(endsFound)


# Sum and print
print(total)