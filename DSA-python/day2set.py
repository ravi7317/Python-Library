# Set example

# Create a set
fruits = {"apple", "banana", "cherry"}
print("Set:", fruits)

# Add and remove elements
fruits.add("orange")
fruits.remove("banana")
print("Updated set:", fruits)

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
print("Symmetric difference:", set_a ^ set_b)
