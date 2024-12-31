import re

with open('input.txt') as f:
    line = f.read()

    # Regex input for valid mul, do and don't instructions
    instructions = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))', line)

    enabled = True
    products = []
    for item in instructions:
        a, b, on, off = item

        # Toggle enabled if necessary
        if on:
            enabled = True
        elif off:
            enabled = False
        
        # Execute mul if enabled and store in a list
        else:
            if enabled:
                products.append((int(a) * int(b)))

    # Sum and print product list
    print(sum(products)) 