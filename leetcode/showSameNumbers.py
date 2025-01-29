numbers = [1, 1, 2, 3, 2]

repeated= []

for num in numbers:
    if numbers.count(num) > 1   and num not in repeated:
        repeated.append(num)
        
print(repeated)        
        