nums = [5, 20, 15, 20, 25, 50, 20]
item = 20

new_list = []

for x in nums:
    if x != item:
        new_list.append(x)

print(new_list)