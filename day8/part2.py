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

# For each pair of antennas of the same type, calculate the location of the antinodes created
antinodes = set()
for l in antennas.values():
   for pos1, pos2 in combinations(l, 2):
        delta = (pos1[0] - pos2[0], pos1[1] - pos2[1])
        counter = 0
        # Check for antinodes behind pos1
        while True:
            antinode = (pos1[0] + delta[0] * counter, pos1[1] + delta[1] * counter)
            if not inGrid(antinode, maxRow, maxCol):
                counter = 0
                break
            counter += 1
            antinodes.add(antinode)
        # Check for antinodes ahead of pos2
        while True:
            antinode = (pos2[0] - delta[0] * counter, pos2[1] - delta[1] * counter)
            if not inGrid(antinode, maxRow, maxCol):
                counter = 0
                break
            counter += 1
            antinodes.add(antinode)

# Print length of antinode set
print(len(antinodes))