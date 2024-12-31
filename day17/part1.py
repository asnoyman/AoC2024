def getCombo(val, A, B, C):
    if val in range(4):
        return val
    elif val == 4:
        return A
    elif val == 5:
        return B
    elif val == 6:
        return C
    exit()


# Set up registers and read program into tuples
A = 0
B = 0
C = 0
program = []
with open('input.txt') as f:
    for line in f.readlines():
        parts = line.split(':')
        if parts[0][-1] == 'A':
            A = int(parts[1][1:])
        if parts[0][-1] == 'B':
            B = int(parts[1][1:])
        if parts[0][-1] == 'C':
            C = int(parts[1][1:])
        
        if line[0] == 'P':
            instructions = parts[1][1:].split(',')
            for i in range(0, len(instructions), 2):
                program.append((int(instructions[i]), int(instructions[i + 1])))


# Run the program
i = 0
output = []
while i < len(program):
    opcode, val = program[i]

    if opcode == 0:
        A //= 2 ** getCombo(val, A, B, C)
    elif opcode == 1:
        B ^= val
    elif opcode == 2:
        B = getCombo(val, A, B, C) % 8
    elif opcode == 3 and A != 0:
        i = val - 1
    elif opcode == 4:
        B ^= C
    elif opcode == 5:
        output.append(getCombo(val, A, B, C) % 8)
    elif opcode == 6:
        B = A // (2 ** getCombo(val, A, B, C))
    elif opcode == 7:
        C = A // (2 ** getCombo(val, A, B, C))
    i += 1

print(','.join([str(num) for num in output]))