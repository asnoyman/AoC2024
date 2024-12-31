from collections import defaultdict

# Convert the line into a list of file_ids and free space
memory = []
with open('input.txt') as f:
    for i, char in enumerate(f.read().strip()):
        if i % 2 == 0:
            for _ in range(int(char)):
                memory.append(i // 2)
        else:
            for _ in range(int(char)):
                memory.append('.')

# Starting with the highest file_id, fill the left most space indices
left = 0
right = len(memory) - 1
while left < right:
    # print(memory, left, right)
    if memory[right] == '.':
        right -= 1
    elif memory[left] != '.':
        left += 1
    else:
        memory[left], memory[right] = memory[right], memory[left]

# Calculate checksum by summing the product of each id and its memory index
checksum = 0
for i, mem in enumerate(memory):
    if mem == '.':
        break

    checksum += i * mem

print(checksum)