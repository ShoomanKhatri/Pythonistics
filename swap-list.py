def swap_elements(lst, index1, index2):
    """Swap two elements in a list at the given indices."""
    if index1 < 0 or index1 >= len(lst) or index2 < 0 or index2 >= len(lst):
        raise IndexError("One or both indices are out of range.")
    
    # The Pythonic one-liner swap (no temp variable needed!)
    lst[index1], lst[index2] = lst[index2], lst[index1]
    
    return lst


# --- Main Execution ---
my_list = [23, 65, 19, 90]
idx1, idx2 = 0, 2

print(f"Original List:    {my_list}")
print(f"Swapping indices: {idx1} and {idx2}")

swap_elements(my_list, idx1, idx2)

print(f"Modified List:    {my_list}")