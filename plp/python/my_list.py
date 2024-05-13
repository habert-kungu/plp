my_list = []

# Append the numbers
my_list.append([10, 20, 30, 40])
print(my_list)  # Output: [[10, 20, 30, 40]]

# Extend the list
my_list[0].extend([50, 60, 70])
print(my_list)  # Output: [[10, 20, 30, 40, 50, 60, 70]]

# Inserting at index 2
my_list[0].insert(2, 15)
print(my_list)  # Output: [[10, 20, 15, 30, 40, 50, 60, 70]]

# Sort the list in place
my_list[0].sort()
print(my_list)  # Output: [[10, 15, 20, 30, 40, 50, 60, 70]]
hello = my_list[0].index(30)

# Find and print the index of the value 30
index_30 = my_list[0].index(30)
print("Index of 30:", index_30)  # Output: Index of 30: 3
