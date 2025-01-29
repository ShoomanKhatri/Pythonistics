numbers = [1, 1, 2, 3, 2]
output = []

for num in numbers:
    if num not in output:  # Check if the number is not already in output
        output.append(num)

print(output)
