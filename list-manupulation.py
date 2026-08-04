my_list = [100, 50, 400, 500]

# Change second element
my_list[1] = 200
print("Updated (Change):", my_list)

# Append 600
my_list.append(600)
print("Updated (Append):", my_list)

# Insert 300 at index 2
my_list.insert(2, 300)
print("Updated (Insert):", my_list)

# Remove 600 (by value)
my_list.remove(600)
print("Updated (Remove 600):", my_list)

# Remove element at index 0
my_list.pop(0)
print("Updated (Remove Index 0):", my_list)