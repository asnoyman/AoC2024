from collections import defaultdict
from itertools import combinations

def inGrid(coords, maxRow, maxCol):
    if coords[0] < 0 or coords[1] < 0 or coords[0] >= maxRow or coords[1] >= maxCol:
        return False
    return True

# Read in map as dict of antenna type to locations
antennas = defaultdict(list)
maxRow = 0
maxCol = 0
with open('input.txt') as f:
    for row, line in enumerate(f.readlines()):
        for col, location in enumerate(line.strip()):
            if location != '.':
                antennas[location].append((row, col))
        maxRow = row + 1
        maxCol = len(line)

# For each pair of antennas of the same type, calculate the location of the two antinodes
antinodes = set()
for l in antennas.values():
   for pos1, pos2 in combinations(l, 2):
        delta = (pos1[0] - pos2[0], pos1[1] - pos2[1])
        anti1 = (pos1[0] + delta[0], pos1[1] + delta[1])
        anti2 = (pos2[0] - delta[0], pos2[1] - delta[1])

        # If in bounds of map, add to antinode set
        if inGrid(anti1, maxRow, maxCol):
            antinodes.add(anti1)
        if inGrid(anti2, maxRow, maxCol):
            antinodes.add(anti2)

# Print length of antinode set
print(len(antinodes))