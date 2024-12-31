# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end_of_word = True

#     def search(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return node.is_end_of_word

# # checkDisplay will return True if the pattern is in the towel type list
# # it will return true if any of the sub calls are true that have used a towel to reduce the display
# # otherwise it will return False
# def checkDisplay(towelTypes, impossibleTypes, display):
#     if towelTypes.search(display):
#         return True

#     if impossibleTypes.search(display):
#         return False

#     for i in range(len(display) - 1, 0, -1):
#         if towelTypes.search(display[:i]):
#             if checkDisplay(towelTypes, impossibleTypes, display[i:]):
#                 towelTypes.insert(display)
#                 return True
#             else:
#                 impossibleTypes.insert(display[i:])

#     impossibleTypes.insert(display)
#     return False


# # Create list of towel types:
# towelTypes = Trie()
# impossibleTypes = Trie()
# possibleDisplays = 0
# with open('input.txt') as f:
#     for i, line in enumerate(f.readlines()):
#         if i == 0:
#             for towelType in list(line.strip().split(', ')):
#                 towelTypes.insert(towelType)
#         elif i > 1:
#             print(line.strip())
#             if checkDisplay(towelTypes, impossibleTypes, line.strip()):
#                 possibleDisplays += 1


# print(possibleDisplays)



# checkDisplay will return True if the pattern is in the towel type list
# it will return true if any of the sub calls are true that have used a towel to reduce the display
# otherwise it will return False
# def checkDisplay(towelTypes, impossibleTypes, display):
#     if display in towelTypes:
#         return True

#     if display in impossibleTypes:
#         return False

#     for i in range(len(display) - 1, 0, -1):
#         if display[:i] in towelTypes:
#             if checkDisplay(towelTypes, impossibleTypes, display[i:]):
#                 towelTypes.add(display)
#                 return True
#             else:
#                 impossibleTypes.add(display[i:])

#     impossibleTypes.add(display)
#     return False


# # Create list of towel types:
# towelTypes = set()
# impossibleTypes = set()
# possibleDisplays = 0
# with open('input.txt') as f:
#     for i, line in enumerate(f.readlines()):
#         if i == 0:
#             for towelType in list(line.strip().split(', ')):
#                 towelTypes.add(towelType)
#         elif i > 1:
#             print(line.strip())
#             if checkDisplay(towelTypes, impossibleTypes, line.strip()):
#                 possibleDisplays += 1

# print(possibleDisplays)


towelTypes = set()
possibleDisplays = 0
with open('input.txt') as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:
            for towelType in list(line.strip().split(', ')):
                towelTypes.add(towelType)
        elif i > 1:
            line = line.strip()
            dp = [0] * (len(line) + 1)
            for i in range(1, len(line) + 1):
                for j in range(i):
                    for towelType in towelTypes:
                        if j + len(towelType) == i and towelType == line[j:i]:
                            if j == 0:
                                dp[i] += 1
                            else:
                                dp[i] += dp[j]
            if dp[-1]:
                possibleDisplays += 1
print(possibleDisplays)