# patterns.py
# Pattern Generation using Nested Loops

# Get pattern size from the user
size = int(input("Enter the size/height: "))

# -----------------------------
# Square Pattern
# -----------------------------
print("\nSquare Pattern:")
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()

# -----------------------------
# Right-Angled Triangle Pattern
# -----------------------------
print("\nRight-Angled Triangle:")
for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# -----------------------------
# Pyramid Pattern
# -----------------------------
print("\nPyramid Pattern:")
for i in range(size):
    # Print spaces
    for j in range(size - i - 1):
        print(" ", end="")

    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")

    print()