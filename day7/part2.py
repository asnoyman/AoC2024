from itertools import product
from math import log, floor

# For each line of input, read the test result and equation numbers
total = 0
with open('input.txt') as f:
    for line in f.readlines():
        testResult = int(line.split(':')[0])
        numbers = [int(num) for num in line.split(':')[1].split()]

        # For each permuation of + and *, see if the test result can be reached
        perms = product(['+', '*', '||'], repeat=len(numbers) - 1)
        for perm in perms:
            result = numbers[0]
            for i, operator in enumerate(perm):
                if operator == '+':
                    result += numbers[i+1]
                elif operator == '*':
                    result *= numbers[i+1]
                elif operator == '||':
                    # Concatenate the two numbers:
                    
                    # Get the number of digits in the new number
                    lengthOfNum = floor(log(numbers[i+1], 10)) + 1
                    # Multiply the current result by 10^length
                    result *= 10 ** lengthOfNum
                    # Add new number
                    result += numbers[i+1]

                    # * Below I thought of a more simple method after finishing the question
                    # result = int(str(result) + str(numbers[i+1]))

            # If the test result is reached, add the test result to the sum
            if result == testResult:
                total += result
                break
        

# Print sum
print(total)