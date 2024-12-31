# Read input into 2D array
word_search = []
with open('input.txt') as f:
    for line in f.readlines():
        word_search.append(line.strip())

tally = 0
lenY = len(word_search)
lenX = len(word_search[0])
dirs = [(i, j) for i in range(-1,2) for j in range(-1,2)]
for i in range(lenY):
    for j in range(lenX):
        # For each X in the array
        if word_search[i][j] == 'X':
            # Search for XMAS in each direction
            for dir in dirs:
                if (
                    i + dir[0] * 3 >= 0 and j + dir[1] * 3 >= 0             # Check left and top bounds
                    and i + dir[0] * 3 < lenY and j + dir[1] * 3 < lenX     # Check right and bottom bounds
                    and word_search[i + dir[0] * 1][j + dir[1] * 1] == 'M'  # Check for M
                    and word_search[i + dir[0] * 2][j + dir[1] * 2] == 'A'  # Check for A
                    and word_search[i + dir[0] * 3][j + dir[1] * 3] == 'S'  # Check for S
                ):
                    # For each found, increment tally
                    tally += 1

print(tally)