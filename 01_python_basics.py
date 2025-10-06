"""
Introduction to Python Basics
This script covers fundamental Python concepts for beginners.
"""

# ============================================
# 1. Variables and Data Types
# ============================================
print("=" * 50)
print("1. Variables and Data Types")
print("=" * 50)

# Numbers
integer_num = 42
float_num = 3.14
print(f"Integer: {integer_num}, Float: {float_num}")

# Strings
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)

# Boolean
is_student = True
print(f"Is student: {is_student}")

# ============================================
# 2. Lists (ordered, mutable collection)
# ============================================
print("\n" + "=" * 50)
print("2. Lists")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]
print(f"Original list: {numbers}")

# Accessing elements
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")

# Adding elements
numbers.append(6)
print(f"After append: {numbers}")

# List slicing
print(f"First three: {numbers[:3]}")

# ============================================
# 3. Dictionaries (key-value pairs)
# ============================================
print("\n" + "=" * 50)
print("3. Dictionaries")
print("=" * 50)

student = {
    "name": "Bob",
    "age": 20,
    "grades": [85, 90, 92]
}
print(f"Student: {student}")
print(f"Name: {student['name']}")
print(f"Grades: {student['grades']}")

# ============================================
# 4. Control Flow (if statements)
# ============================================
print("\n" + "=" * 50)
print("4. Control Flow")
print("=" * 50)

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Score: {score}, Grade: {grade}")

# ============================================
# 5. Loops
# ============================================
print("\n" + "=" * 50)
print("5. Loops")
print("=" * 50)

# For loop
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"  {i}")

# While loop
print("Countdown:")
count = 3
while count > 0:
    print(f"  {count}")
    count -= 1
print("  Blast off!")

# ============================================
# 6. Functions
# ============================================
print("\n" + "=" * 50)
print("6. Functions")
print("=" * 50)

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

grades = [85, 90, 92, 88, 95]
avg = calculate_average(grades)
print(f"Grades: {grades}")
print(f"Average: {avg:.2f}")

# ============================================
# 7. List Comprehensions
# ============================================
print("\n" + "=" * 50)
print("7. List Comprehensions")
print("=" * 50)

# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares (traditional): {squares}")

# List comprehension (more Pythonic)
squares = [i ** 2 for i in range(1, 6)]
print(f"Squares (comprehension): {squares}")

# Filtering with list comprehension
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(f"Even squares: {even_squares}")

print("\n" + "=" * 50)
print("Python Basics Complete!")
print("=" * 50)
