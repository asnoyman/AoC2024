# Read in the data into 2 lists
listA = []
listB = []
with open('input.txt') as f:
    for line in f.readlines():
        a, b = line.split()
        listA.append(int(a))
        listB.append(int(b))

# Sort the lists
listA.sort()
listB.sort()

# Sum the differences between the same index in each list
length = len(listA)
result = [abs(listA[i] - listB[i]) for i in range(length)]

print(sum(result))