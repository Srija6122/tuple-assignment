# number_pattern.py
# Program to generate a number triangle pattern with input validation

def print_number_pattern(size):
    # Generate a number triangle pattern
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

try:
    size = int(input("Enter the size of the pattern: "))

    if size <= 0:
        print("Error: Please enter a positive integer.")
    else:
        print("\nNumber Pattern:")
        print_number_pattern(size)

except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")