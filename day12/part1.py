class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.edges = []
        self.visited = False

    def __repr__(self):
        return f'{self.value}, {[e.value for e in self.edges]}'

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
            node.edges.append(graph[i-1][j])
        if i + 1 < len(graph) and graph[i+1][j].value == node.value:
            node.edges.append(graph[i+1][j])
        if j - 1 >= 0 and graph[i][j-1].value == node.value:
            node.edges.append(graph[i][j-1])
        if j + 1 < len(graph[0]) and graph[i][j+1].value == node.value:
            node.edges.append(graph[i][j+1])

# print(*graph, sep='\n', end='\n\n')

# For each group, calculate perimeter and area
total = 0
for row in graph:
    for node in row:
        area = 0
        perimeter = 0
        stack = [node]
        while len(stack):
            n = stack.pop()
            if n.visited:
                continue
            n.visited = True
            area += 1
            perimeter += 4 - len(n.edges)
            stack += n.edges

        total += area * perimeter

# Print the sum of the products of each P and A
print(total)