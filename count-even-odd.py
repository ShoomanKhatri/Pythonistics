numbers = [10, 21, 4, 45, 66, 93, 11]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)