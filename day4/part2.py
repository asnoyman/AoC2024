# Read input into 2D array
word_search = []
with open('input.txt') as f:
    for line in f.readlines():
        word_search.append(line.strip())

tally = 0
lenY = len(word_search)
lenX = len(word_search[0])
for i in range(lenY):
    for j in range(lenX):
        # For each A in the array
        if word_search[i][j] == 'A':
            # Search for M and S on both diagonals
                if (
                    i - 1 >= 0 and j - 1 >= 0             # Check left and top bounds
                    and i + 1 < lenY and j + 1 < lenX     # Check right and bottom bounds
                    and set((word_search[i - 1][j - 1], word_search[i + 1][j + 1])) == set(('M', 'S'))  # Check negative diagonal
                    and set((word_search[i - 1][j + 1], word_search[i + 1][j - 1])) == set(('M', 'S'))  # Check positive diagonal
                ):
                    # For each found, increment tally
                    tally += 1

print(tally)