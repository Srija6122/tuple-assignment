# nested_while_loop.py
# This program demonstrates the use of nested while loops.
# The outer while loop controls the number of rows,
# and the inner while loop prints ascending numbers in each row.

# Get the number of rows from the user
rows = int(input("Enter the number of rows: "))

# Outer while loop
i = 1
while i <= rows:
    # Inner while loop
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1