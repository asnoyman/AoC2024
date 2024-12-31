from collections import defaultdict

# Read the input into 2 dictionaries
dictA = defaultdict(int)
dictB = defaultdict(int)
with open('input.txt') as f:
    for line in f.readlines():
        a, b = line.split()
        dictA[int(a)] += 1
        dictB[int(b)] += 1

# Multiply the count key of the first dict by the value of it in the first dict and second dict
result = [key * dictA[key] * dictB[key] for key in dictA.keys()]

# Sum the results and print
print(sum(result))