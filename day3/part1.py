import re

with open('input.txt') as f:
    line = f.read()

    # Regex input for valid mul instructions
    instructions = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line)

    # Execute each one and store in a list
    products = []
    for item in instructions:
        a, b = re.findall(r'[0-9]{1,3}', item)
        products.append((int(a) * int(b)))

    # Sum and print product list
    print(sum(products))