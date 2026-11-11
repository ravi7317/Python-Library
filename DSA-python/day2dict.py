# Dictionary example

student = {
    "name": "Alex",
    "age": 20,
    "course": "DSA",
}

print(student)
print("Name:", student["name"])

# Add and update values
student["grade"] = "A"
student["age"] = 21

# Remove a value
removed_grade = student.pop("grade")

print("Updated student:", student)
print("Removed grade:", removed_grade)
