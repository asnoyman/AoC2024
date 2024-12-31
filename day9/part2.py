from collections import defaultdict

# Convert the line into a list of tuples of (file_id, size)
memory = []
with open('input.txt') as f:
    for i, char in enumerate(f.read().strip()):
        if i % 2 == 0:
            memory.append((i // 2, int(char)))
        else:
            memory.append(('.', int(char)))

# Starting with the highest file_id, fill the left most space indices by moving whole files
left = 0
right = len(memory) - 1
while left < right:
    if memory[right][0] == '.':
        right -= 1
    elif memory[left][0] != '.':
        left += 1
    else:
        swappedWithSpace = False
        for i in range(left, right):
            # If the memory block at i is filled then continue
            if memory[i][0] != '.':
                continue
            
            # If the memory block is too small then continue
            if memory[i][1] < memory[right][1]:
                continue
            # If the memory block is equal size then swap the memory and emptySpace
            elif memory[i][1] == memory[right][1]:
                memory[i], memory[right] = memory[right], memory[i]
                break
            
            # If the memory block is greater then swap the memory and emptySpace
            # and add a new memory block after the new left block with the difference
            #! Do not decrement the right pointer if this happens as a new block is added to its left,
            #! effectively decrementing the position already
            elif memory[i][1] > memory[right][1]:
                extraSpace = memory[i][1] - memory[right][1]
                memory[i], memory[right] = memory[right], memory[i]
                memory[right] = (memory[right][0], memory[i][1])
                memory.insert(i + 1, ('.', extraSpace))
                swappedWithSpace = True
                break

        if not swappedWithSpace:
            right -= 1

# Calculate checksum by summing the product of each memory index and its file id
checksum = 0
memLength = 0
for mem in memory:
    if mem[0] != '.':
        checksum += sum(range(memLength, memLength + mem[1])) * mem[0]
    memLength += mem[1]

print(checksum)