# from collections import defaultdict

# def getCombo(val, A, B, C):
#     if val in range(4):
#         return val
#     elif val == 4:
#         return A
#     elif val == 5:
#         return B
#     elif val == 6:
#         return C
#     exit()


# # Set up registers and read program into tuples
# startingA = 0
# startingB = 0
# startingC = 0
# program = []
# expected_output = []
# with open('input.txt') as f:
#     for line in f.readlines():
#         parts = line.split(':')
#         if parts[0][-1] == 'A':
#             continue
#         if parts[0][-1] == 'B':
#             startingB = int(parts[1][1:])
#         if parts[0][-1] == 'C':
#             startingC = int(parts[1][1:])
        
#         if line[0] == 'P':
#             instructions = parts[1][1:].split(',')
#             for i in range(0, len(instructions), 2):
#                 program.append((int(instructions[i]), int(instructions[i + 1])))
#                 expected_output.append(int(instructions[i]))
#                 expected_output.append(int(instructions[i + 1]))

# def runProgram(startingA, forBitmap=False):
#     A = startingA
#     B = 0
#     C = 0
#     i = 0
#     output = []
#     while i < len(program):
#         opcode, val = program[i]

#         if opcode == 0:
#             A >>= getCombo(val, A, B, C)
#         elif opcode == 1:
#             B ^= val
#         elif opcode == 2:
#             B = getCombo(val, A, B, C) % 8
#         elif opcode == 3 and A != 0:
#             i = val - 1
#         elif opcode == 4:
#             B ^= C
#         elif opcode == 5:
#             output.append(getCombo(val, A, B, C) % 8)
#             if forBitmap:
#                 return output
#         elif opcode == 6:
#             B = A >> getCombo(val, A, B, C)
#         elif opcode == 7:
#             C = A >> getCombo(val, A, B, C)
#         i += 1
    
#     return output

# # Run the program
# bitmaps = defaultdict(list)
# for startingA in range(2 ** 12, 2 ** 13):
#     output = runProgram(startingA, True)[0]
#     bitmaps[output].append(startingA)

# optionsForA = [num for num in bitmaps[expected_output[0]]]
# print(optionsForA)
# for num in expected_output[1:]:
#     tempOptionsForA = []
#     for option in optionsForA:
#         for bitmap in bitmaps[num]:
#             if ((bitmap & 0b1111111000) >> 3) == (option & 0b0001111111):
#                 tempOptionsForA.append(((option & 0b1110000000) << 3) + bitmap)
#     optionsForA = tempOptionsForA
#     print(num, len(optionsForA))
# print(sorted(optionsForA))




from collections import namedtuple
from dataclasses import dataclass, field
from typing import Optional


class BitPattern(namedtuple("BitPattern", ["mask", "pattern"])):
    def merge(self, other: "BitPattern") -> Optional["BitPattern"]:
        # to be compatible, all the bits constrained by _both_ patterns must match
        common_mask = self.mask & other.mask
        if (self.pattern & common_mask) == (other.pattern & common_mask):
            return BitPattern(self.mask | other.mask, self.pattern | other.pattern)

        # Not compatible
        return None

    def __lshift__(self, other: int):
        return BitPattern(self.mask << other, self.pattern << other)

    def __repr__(self):
        """
        Shows the masked pattern with 0 or 1 for the constrained bits and
        "." for the unconstrained ones.
        """
        mask_bin = "{:010b}".format(self.mask)
        # if the mask is more than 10 bits, zero-pad the pattern to the same length
        pat_bin = ("{:0" + str(len(mask_bin)) + "b}").format(self.pattern)
        return (
            "BitPattern("
            + "".join("." if m == "0" else p for m, p in zip(mask_bin, pat_bin))
            + ")"
        )


@dataclass
class Machine:
    program: list[int]
    a: int
    b: int
    c: int
    ptr: int = 0

    output: list[int] = field(default_factory=list, init=False)

    def __post_init__(self):
        # Store operation methods indexable by opcode
        self.operations = (
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv,
        )

    def __repr__(self):
        pr_it = iter(self.program)
        prg = []
        i = 0
        for opcode, operand in zip(pr_it, pr_it):
            prg.append(
                (">" if self.ptr == i else " ")
                + self.operations[opcode].__name__
                + " "
                + str(operand)
            )
            i += 2

        return (
            ";".join(prg) + "\n" + f"   {self.a=}, {self.b=}, {self.c=}, {self.output=}"
        )

    def combo(self, operand):
        if operand < 0 or operand > 6:
            raise ValueError(f"Invalid combo operand {operand}")
        if operand == 4:
            return self.a
        if operand == 5:
            return self.b
        if operand == 6:
            return self.c
        return operand

    def rightshift_a(self, operand):
        return self.a >> self.combo(operand)

    def run(self, init_a=None, debug=False):
        self.output = []
        self.ptr = 0
        saved_registers = (self.a, self.b, self.c)
        if init_a is not None:
            self.a = init_a
        while self.ptr < len(self.program):
            result = self.operations[self.program[self.ptr]](self.program[self.ptr + 1])
            if result is None:
                self.ptr += 2
            else:
                self.ptr = result

            # debugging
            if debug:
                print(self)

        output_equals_program = self.output == self.program

        self.a, self.b, self.c = saved_registers
        return output_equals_program

    # operations

    def adv(self, operand):
        self.a = self.rightshift_a(operand)

    def bdv(self, operand):
        self.b = self.rightshift_a(operand)

    def cdv(self, operand):
        self.c = self.rightshift_a(operand)

    def bxl(self, operand):
        self.b = self.b ^ operand

    def bst(self, operand):
        self.b = self.combo(operand) % 8

    def jnz(self, operand):
        if self.a == 0:
            return
        return operand

    def bxc(self, operand):
        self.b = self.b ^ self.c

    def out(self, operand):
        self.output.append(self.combo(operand) % 8)


def generate_base_patterns(machine: Machine) -> list[set[BitPattern]]:
    patterns = []
    # Magic constants from the input program
    k1 = machine.program[3]
    k2 = machine.program[7]
    for n in range(8):
        n_patterns = set()
        for b in range(8):
            # constraint on the lowest three bits
            b_pattern = BitPattern(7, b ^ k1 ^ k2)
            # constraint on some set of three other bits somewhere between
            # positions 0 and 10
            c_pattern = BitPattern(7, n ^ b) << (b ^ k2)
            merged = b_pattern.merge(c_pattern)
            if merged:
                n_patterns.add(merged)
        patterns.append(n_patterns)

    return patterns


# See README for explanation
def quine(machine: Machine):
    base_patterns = generate_base_patterns(machine)
    # Debug base patterns
    print("Base patterns:")
    for n, pats in enumerate(base_patterns):
        print(n)
        print(*pats, sep="\n")

    candidates = set(base_patterns[machine.program[0]])
    for i in range(1, len(machine.program)):
        target_value = machine.program[i]
        new_candidates = set()
        # Patterns for this digit will constrain bits starting at position 3i
        # (counting from the right)
        this_number_patterns = set(p << (3 * i) for p in base_patterns[target_value])
        # attempt to merge each of the new patterns for this digit with each of the
        # existing patterns for the sequence so far, discarding any that conflict.
        for tail_pattern in candidates:
            for pattern in this_number_patterns:
                merged = tail_pattern.merge(pattern)
                if merged:
                    new_candidates.add(merged)

        if not new_candidates:
            raise ValueError("This program cannot generate itself")

        candidates = new_candidates
        print(f"{len(candidates)} candidates remain after iteration {i}")

    # we now have all the patterns that could match an initial "a" register,
    # the smallest number that could match any of these patterns happens to be
    # exactly the decimal value of the smallest pattern, since we've been
    # careful to ensure that all non-constrained bits in every pattern are
    # left as zero at all steps
    return min(p.pattern for p in candidates)


def load_data():
    with open("input.txt", "r") as f:
        r_a = int(f.readline()[12:])
        r_b = int(f.readline()[12:])
        r_c = int(f.readline()[12:])

        # skip blank line
        f.readline()
        program_str = f.readline()[9:]

    return Machine(
        program=[int(i) for i in program_str.split(",")], a=r_a, b=r_b, c=r_c
    )


def main():
    m = load_data()
    # part 1
    m.run(debug=True)
    print("Output:", "".join(str(i) for i in m.output))

    # part 2
    print(f"Minimum quine seed: {quine(m)}")


if __name__ == "__main__":
    main()